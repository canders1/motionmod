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

def initWPriors(wList):
	wProbs = []
	for w in range(0,len(wList)):
		wProbs.append(1/float(len(wList)))
	return wProbs

def initCPriors(eList):
	cProbs = [0.4,0.4,0.1,0.1]
	return cProbs

def lzero(w,m,wProbs,wVecs):
	posterior = wVecs[w][m] * wProbs[w]
	return posterior

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

def makeCS(eList):
	cs = []
	indexes = range(0,len(eList))
	for i in range(0,len(eList)):
		cs += list(itertools.combinations(indexes,i+1))
	cs = [list(x) for x in cs]
	return cs

def makeObservation(cs):
	o = random.choice(cs)
	print o
	return o

def main():
	wfile = sys.argv[1]
	efile = sys.argv[2]
	pfile = sys.argv[3]
	eList,eDict = parseEntities(efile)
	pList,pDict = parsePropositions(pfile)
	wList,wDict,wVecs = parseWorlds(wfile)
	wProbs = initWPriors(wList)
	cProbs = initCPriors(eList)
	lzero(1,1,wProbs,wVecs)
	lzero(1,0,wProbs,wVecs)
	updateWorld(1,"speaker in Amherst",eList,wProbs,wVecs,cProbs,pDict,pList)
	updatePerspective(3,"X in Amherst",cProbs,wList,eList,wProbs,wVecs,pDict,pList)
	cs = makeCS(eList)
	makeObservation(cs)
main()

