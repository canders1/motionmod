from __future__ import division
import sys
import re
import itertools
import random
from messageClass import Message
from worldClass import World
import copy

def expandMessages(u,aList,pList,eDict,gaps):
	#Generates all possible messages given an utterance with gaps
	#The gaps can be plugged by any entity in the relevant ontological class
	messageList = [[u,aList,pList]]
	for gap in gaps:
		subList = eDict[gap]
		newMessageList = []			
		for m in messageList:
			currU = m[0]
			currA = m[1]
			currP = m[2]
			if gap not in currU:
				newMessageList.append(m)
			else:
				for sub in subList:
					newU = re.sub(gap,sub,currU)
					newAList = []
					newPList = []
					for a in range(0,len(currA)):
						newAList.append(re.sub(gap,sub,currA[a]))
					for p in range(0,len(currP)):
						newPList.append(re.sub(gap,sub,currP[p]))
					newMessageList.append([newU,newAList,newPList])
		messageList = newMessageList
	return messageList

def parseMessages(mfile,eDict):
	mDict = {}
	mList = []
	mf = open(mfile,"r")
	messages = mf.read().split("\n")
	for m in messages:
		mContents = m.split("&")
		utterance = mContents[0]
		assertions = mContents[1].split("\t")
		presuppositions = mContents[2].split("\t")
		gaps = mContents[3].split(",")
		expandedMList = expandMessages(utterance,assertions,presuppositions,eDict,gaps)
		for exM in expandedMList:
			mDict,mList = insertMessages(exM,mDict,mList)
	return mDict,mList

def insertMessages(m,mDict,mList):
	u = m[0]
	a = m[1]
	p = m[2]
	mObject = Message(u,a,p)
	mDict[len(mList)] = mObject
	mList.append(mObject)
	return mDict,mList

def parseEntities(efile):
	eDict = {}
	ef = open(efile,"r")
	entLines = ef.read().split("\n")
	for e in entLines:
		entry = e.split("\t")
		name = entry[0]
		entries = entry[1].split(",")
		eDict[name] = entries
	return eDict

def parsePredicates(prfile):
	predList = []
	prf = open(prfile,"r")
	prLines = prf.read().split("\n")
	for pr in prLines:
		prs = pr.split("\t")
		name = prs[0]
		args = prs[1].split(",")
		exclusives = prs[2].split(",")
		predList.append([name,args,exclusives])
	return predList

def genPropSet(pred,eDict):
	#Generates all possible propositions given a predicate and a entity dictionary
	name = pred[0]
	args = pred[1]
	ex = pred[2]
	predList = [args]
	for e in range(0,len(args)):
		arg = args[e]
		if arg not in ex:
			expandedList = []
			for pred in predList:
				possibilities = eDict[arg]
				for poss in possibilities:
					newArgs = copy.copy(pred)
					newArgs[e] = poss
					expandedList.append(newArgs)
		predList = expandedList
	if ex != ['']:
		for e in ex:
			exList = []
			possibilities = eDict[e]
			for pred in predList:
				expandedList = []
				for p in possibilities:
					newArgs = [p if x==e else x for x in pred]
					expandedList.append(newArgs) 
				exList.append(map(lambda x: [name]+x,expandedList))
		predList = exList
	else:
		predList = map(lambda x: [[name]+x],predList)
	return predList


def genWorlds(predList,eDict):
	#Generates all possible worlds given a list of predicates and entities
	wDict = {}
	predSet = []
	wSet = [World("0")]
	for p in predList:
		predSet += genPropSet(p,eDict) #Generate all possible propositions
	for pSet in predSet:
		if len(pSet) == 1:
			#Free choice, add some or all
			prop = pSet[0]
			newWSet =[]
			for w in wSet:
				newW = w.copy()
				newW.addProposition(prop[0]+prop[1])
				newWSet.append(newW)
			wSet += newWSet
		else:
			#Forced choice (mutually exclusive options, one must be true)
			newWorlds = []
			for choice in pSet:
				newWSet = []
				for w in wSet:
					newW = w.copy()
					newW.addProposition(choice[0]+choice[1])
					newWSet.append(newW)
				newWorlds += newWSet
			wSet = newWorlds
	return wDict,wSet

def initWPriors(wList):
	wProbs = []
	for w in range(0,len(wList)):
		wProbs.append(1/float(len(wList)))
	return wProbs

def initCPriors(eList):
	return urn(eList)

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

def initPriors(wList,eList):
	print "initializing world probs"
	wProbs = initWPriors(wList)
	print "initializing perspective probs"
	cProbs = initCPriors(eList)
	cs = range(0,len(wList))
	return wProbs,cProbs,cs

def evaluate(wProbs,cProbs,cs, label):
	print label+" max world prob: ", max(wProbs)
	print label+" min world prob: ", min(wProbs)
	print label+" perspective probs: ", cProbs
	print label+" size of context set: ", len(cs)
	return

def utter(perspList,eDict,wList,wDict,wProbs,cProbs,cs,mList,mDict):
	observation = makeObservation(cs)
	message = speaker0(observation,wProbs,cProbs,mList,mDict,perspList)
	for w in range(0,len(wList)):
		wProbs[w] = updateWorld(w,message,eList,wProbs,cProbs,pDict,pList)
	for e in range(0,len(eList)):
		cProbs[e] = updatePerspective(e,message,cProbs,wList,eList,wProbs,pDict,pList)
	cs = updateCS(wProbs)
	return normProbs(wProbs),normProbs(cProbs),cs

def makeObservation(cs):
	size = random.randint(1,len(cs))
	sample = random.sample(cs,size)
	return sample

def speaker0(o,wProbs,cProbs,mList,mDict,perspList):
	mProbs = []
	for m in range(0,len(mList)):
		print "Considering ",mList[m]
		mProb = 0.0
		for w in o:
			for per in range(0,len(perspList)):
				prop = getPerspective(per,m,mList,mDict,perspList)
				mProb += listener0(w,prop,wProbs,wVecs)
		mProbs.append(mProb)
	best = 0
	for p in range(0,len(mProbs)):
		if mProbs[p] > mProbs[best]:
			best = p
	print "Message probabilities: ", mProbs
	print "Chosen message is: ",pList[best]
	return best

def getPerspective(p,m,mList,mDict,perspList):
	print perspList[p]
	print mList[m]
	sub = re.sub("X", perspList[p], mList[m])
	subdex = mDict[sub]
	return subdex

def main():
	if len(sys.argv) < 3:
		print "Usage: python assertion.py entities messages predicates"
		quit()
	efile = sys.argv[1]
	mfile = sys.argv[2]
	prfile = sys.argv[3]
	eDict = parseEntities(efile)
	mDict,mList= parseMessages(mfile,eDict)
	predList = parsePredicates(prfile)
	perspList = eDict["SUBJ"]
	wDict,wList = genWorlds(predList,eDict)
	wProbs,cProbs,cs = initPriors(wList,perspList)
	evaluate(wProbs,cProbs,cs, "Initial")
	wProbs,cProbs,cs = utter(perspList,eDict,wList,wDict,wProbs,cProbs,cs,mList,mDict)
	
main()