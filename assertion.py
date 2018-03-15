from __future__ import division
import sys
import re
import itertools
import random

def parseEntities(efile):
	eDict = {}
	eList = []
	ef = open(efile, 'r')
	entities = ef.read().split("\n")
	for e in entities:
		entity = e.split("\t")
		eDict[entity[0]] = len(eList)
		eList.append(entity[0])
	return eList,eDict

def parsePropositions(pfile):
	pDict = {}
	pList = []
	pf = open(pfile,"r")
	props = pf.read().split("\n")
	for p in props:
		prop = p.split("\t")
		pDict[prop[1]] = len(pList)
		pList.append(prop[1])
	return pList,pDict

def parseWorlds(wfile):
	wDict = {}
	wList = []
	wVecs = []
	wf = open(wfile,"r")
	worlds = wf.read().split("\n")
	for w in worlds[1:len(worlds)]:  #Because of comment-line, fix this
		world = w.split("\t")
		wname = world[0]
		wvec = [int(x) for x in world[1:len(world)]]
		wDict[wname] = len(wList)
		wList.append(wname)
		wVecs.append(wvec)
	return wList,wDict,wVecs

def urn(eList,it=100,mixProb=0.4):
	probs = []
	urn = [0,0,1] #Adjust bias towards speaker and addressee here
	eIndexes = range(0,len(eList))
	for i in range(0,it):
		flip = random.random()
		if flip > mixProb:
			urn.append(random.choice(eIndexes))
		else:
			urn.append(random.choice(urn))
	norm = sum(map(int,urn))
	for e in range(0,len(eList)):
		probs.append(urn.count(e)/norm)
	return probs

def initWPriors(wList):
	wProbs = []
	for w in range(0,len(wList)):
		wProbs.append(1/float(len(wList)))
	return wProbs

def initCPriors(eList):
	return urn(eList)
	#return [0.4,0.4,0.1,0.1]

def listener0(w,m,wProbs,wVecs):
	posterior = wVecs[w][m] * wProbs[w]
	return posterior

def speaker0(o,wProbs,wVecs,cProbs,mList,eList,pDict,pList):
	#argmax listener0(w|m) - cost(m)
	print "Observation", o
	mProbs = []
	for m in range(0,len(mList)):
		print "Considering ",mList[m]
		mProb = 0.0
		for w in o:
			for e in range(0,len(eList)):
				prop = getPerspective(e,m,pDict,mList,eList)
				mProb += listener0(w,prop,wProbs,wVecs)
		mProbs.append(mProb)
	best = 0
	for p in range(0,len(mProbs)):
		if mProbs[p] > mProbs[best]:
			best = p
	print "Message probabilities: ", mProbs
	print "Chosen message is: ",pList[best]
	return best

def getPerspective(e,m,pDict,mList,eList):
	sub = re.sub("X", eList[e], mList[m])
	subdex = pDict[sub]
	return subdex

def updateWorld(w,m,eList,wProbs,wVecs,cProbs,pDict,mList):
	posterior = 0.0
	for e in range(0,len(eList)):
		prop = getPerspective(e,m,pDict,mList,eList)
		posterior += cProbs[e]*listener0(w,prop,wProbs,wVecs)
	return posterior

def updatePerspective(e,m,cProbs,wList,eList,wProbs,wVecs,pDict,mList):
	postSum = 0.0
	prop = getPerspective(e,m,pDict,mList,eList)
	for w in range(0,len(wList)):
		postSum += listener0(w,prop,wProbs,wVecs)
	posterior = postSum*cProbs[e]
	return posterior

def makeCS(indexes):
	cs = []
	for i in range(0,len(indexes)):
		cs += list(itertools.combinations(indexes,i+1))
	cs = [list(x) for x in cs]
	return cs

def makeObservation(cs):
	o = random.choice(cs)
	return o

def updateCS(wProbs):
	currW = []
	for w in range(0,len(wProbs)):
		if wProbs[w] > 0.0:
			currW.append(w)
	return makeCS(currW)

def initPriors(wList,eList):
	wProbs = initWPriors(wList)
	cProbs = initCPriors(eList)
	cs = makeCS(range(0,len(wList)))
	return wProbs,cProbs,cs

def normProbs(probs):
	norm = sum(probs)
	return [(p/norm) for p in probs]

def utter(eList,eDict,pList,pDict,wList,wDict,wVecs,wProbs,cProbs,cs,mList):
	observation = makeObservation(cs)
	message = speaker0(observation,wProbs,wVecs,cProbs,mList,eList,pDict,pList)
	for w in range(0,len(wList)):
		wProbs[w] = updateWorld(w,message,eList,wProbs,wVecs,cProbs,pDict,pList)
	for e in range(0,len(eList)):
		cProbs[e] = updatePerspective(e,message,cProbs,wList,eList,wProbs,wVecs,pDict,pList)
	cs = updateCS(wProbs)
	return normProbs(wProbs),normProbs(cProbs),cs

def evaluate(wProbs,cProbs,cs, label):
	print label+" world probs: ", wProbs
	print label+" perspective probs: ", cProbs
	print label+" size of context set: ", len(cs)
	return

def main():
	if len(sys.argv) < 4:
		print "Usage: python assertion.py worlds entities propositions messages"
		quit()
	wfile = sys.argv[1]
	efile = sys.argv[2]
	pfile = sys.argv[3]
	mfile = sys.argv[4]
	eList,eDict = parseEntities(efile)
	pList,pDict = parsePropositions(pfile)
	wList,wDict,wVecs = parseWorlds(wfile)
	mList, mDict = parsePropositions(mfile)
	wProbs,cProbs,cs = initPriors(wList,eList)
	evaluate(wProbs,cProbs,cs, "Initial")
	wProbs,cProbs,cs = utter(eList,eDict,pList,pDict,wList,wDict,wVecs,wProbs,cProbs,cs,mList)
	evaluate(wProbs,cProbs,cs, "New")
	wProbs,cProbs,cs = utter(eList,eDict,pList,pDict,wList,wDict,wVecs,wProbs,cProbs,cs,mList)
	evaluate(wProbs,cProbs,cs, "New")
main()

