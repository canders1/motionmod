from __future__ import division
import sys

def parseEntities(efile):
	eDict = {}
	eList = []
	ef = open(efile, 'r')
	entities = ef.read().split("\n")
	for e in entities:
		entity = e.split("\t")
		eDict[len(eList)] = entity[0]
		eList.append(entity[0])
	return eList,eDict

def parsePropositions(pfile):
	pDict = {}
	pList = []
	pf = open(pfile,"r")
	props = pf.read().split("\n")
	for p in props:
		prop = p.split("\t")
		pDict[len(pList)] = prop[1]
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
		wDict[len(wList)] = wname
		wList.append(wname)
		wVecs.append(wvec)
	return wList,wDict,wVecs

def initWPriors(wList):
	wProbs = []
	for w in range(0,len(wList)):
		wProbs.append(1/float(len(wList)))
	return wProbs

def initCPriors(eList):
	cProbs = []
	return cProbs

def main():
	wfile = sys.argv[1]
	efile = sys.argv[2]
	pfile = sys.argv[3]
	eList,eDict = parseEntities(efile)
	pList,pDict = parsePropositions(pfile)
	wList,wDict,wVecs = parseWorlds(wfile)
	wProbs = initWPriors(wList)
	cProbs = initCPriors(eList)

main()

