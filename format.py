import sys
import re

def get_data(data):
	probDict = {}
	currSent = ''
	for line in data:
		if line != 'Marginal:\n':
			line = line.strip()
			if line[0] != '{':
				currSent = line
				probDict[currSent] = []
			else:
				currProbs = probDict[currSent]
				if line not in currProbs:
					currProbs.append(line)
					probDict[currSent] = currProbs
	return probDict

def sep_data(ddict):
	sents = ddict.keys()
	worldNames = {}
	probDict = {}
	for s in sents:
		probDict[s] = {}
		assert len(ddict[s]) == 1
		print s
		data = ddict[s][0].split(',\"support\":')
		probs = data[0].replace("{\"probs\":","").strip("[]").split(',')
		support = data[1]
		support = support.replace(']]} : 1','').strip('[').split('],[')
		for i in range(0,len(support)):
			w = support[i]
			p = probs[i]
			if w not in worldNames:
				worldNames[w] = len(worldNames.keys())
			pdict = probDict[s]
			pdict[w] = p
        	probDict[s] = pdict
	for s in sents:
		for w in worldNames.keys():
			if w not in probDict[s]:
				pdict = probDict[s]
				pdict[w] = 0
				probDict[s] = pdict
		for w in probDict[s].keys():
			print s
			print w
			print probDict[s][w]



def main():
	if len(sys.argv) < 2:
  		print "Usage: python format.py filename"
	else:
  		data = open(sys.argv[1],'r').readlines()
  		data = data[0:len(data)-1]
  		probDict = get_data(data)
  		sep_data(probDict)

main()