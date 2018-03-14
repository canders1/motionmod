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
	for i in it:
		flip = random.float(0,1) #figure out how to get a random float in range
		if flip > mixProb:
			urn.append(random.choice(eList))
		else:
			urn.append(random.choice(urn))
	norm = sum(urn)
	for e in range(0,len(eList)):
		probs[e] = count(urn,e)/norm #figure out how to count number of occurences of e in list
	return probs

def initWPriors(wList):
	wProbs = []
	for w in range(0,len(wList)):
		wProbs.append(1/float(len(wList)))
	return wProbs

def initCPriors(eList):
	return urn(eList)

def listener0(w,m,wProbs,wVecs):
	posterior = wVecs[w][m] * wProbs[w]
	return posterior

def speaker0(o,wProbs,wVecs,cProbs,pList):
	#argmax listener0(w|m) - cost(m)
	print "Observation", o
	mProbs = []
	for p in range(0,len(pList)):
		print "Considering ",pList[p]
		mProb = 0.0
		for w in o:
			mProb += listener0(w,p,wProbs,wVecs)
		mProbs.append(mProb)
	best = 0
	for p in range(0,len(mProbs)):
		if mProbs[p] > mProbs[best]:
			best = p
	print "Chosen message is: ",pList[p]
	return p	

def getPerspective(e,m,pDict,wList,eList):
	sub = re.sub("X", eList[e], m)
	subdex = pDict[sub]
	return subdex

def updateWorld(w,m,eList,wProbs,wVecs,cProbs,pDict,pList):
	posterior = 0.0
	for e in range(0,len(eList)):
		prop = getPerspective(e,m,pDict,pList,eList)
		posterior += cProbs[e]*lzero(w,prop,wProbs,wVecs)
	return posterior

def updatePerspective(e,m,cProbs,wList,eList,wProbs,wVecs,pDict,pList):
	postSum = 0.0
	prop = getPerspective(e,m,pDict,pList,eList)
	for w in range(0,len(wList)):
		postSum += lzero(w,prop,wProbs,wVecs)
	posterior = postSum*cProbs[e]
	return posterior

def makeCS(wList):
	cs = []
	indexes = range(0,len(wList))
	for i in range(0,len(wList)):
		cs += list(itertools.combinations(indexes,i+1))
	cs = [list(x) for x in cs]
	return cs

def makeObservation(cs):
	o = random.choice(cs)
	return o

def updateCS(wProbs):
	currW = []
	for w in range(0,len(wProbs)):
		if wProbs[w] > 0:
			currW.append(w)
	return makeCS(currW)

def initPriors(wList,eList):
	wProbs = initWPriors(wList)
	cProbs = initCPriors(eList)
	cs = makeCS(wList)
	return wProbs,cProbs,cs

def utter(eList,eDict,pList,pDict,wList,wDict,wVecs,wProbs,cProbs,cs):
	observation = makeObservation(cs)
	message = speaker0(observation,wProbs,wVecs,cProbs,pList)
	for w in range(0,len(wList)):
		wProbs[w] = updateWorld(w,message,eList,wProbs,wVecs,cProbs,pDict,pList)
	for e in range(0,len(eList)):
		cProbs[e] = updatePerspective(e,message,cProbs,wList,eList,wProbs,wVecs,pDict,pList)
	cs = updateCS(wProbs)
	return wProbs,cProbs,cs

def main():
	wfile = sys.argv[1]
	efile = sys.argv[2]
	pfile = sys.argv[3]
	eList,eDict = parseEntities(efile)
	pList,pDict = parsePropositions(pfile)
	wList,wDict,wVecs = parseWorlds(wfile)
	wProbs,cProbs,cs = initPriors(wList,eList)
	wProbs,cProbs,cs = utter(eList,eDict,pList,pDict,wList,wDict,wProbs,cProbs,cs)
main()

