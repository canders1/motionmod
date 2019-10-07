import sys

def write_results(outlines,nogop,outputfile):
	with open(outputfile,'w') as wf:
		wf.write('#nogop,cost,utterance,perspective,locSam, locLucy, moveLucyNoho, moveSamNoho, moveThelmaNoho,prob\n')
		for l in outlines:
			wf.write(','.join([nogop]+l)+'\n')
	return

def main():
	if len(sys.argv) < 4:
		print("Usage: python parse_results inputfile nogop outputfile")
		return
	#world property order: locSam, locLucy, moveLucyNoho, moveSamNoho, moveThelmaNoho
	data = open(sys.argv[1],'r').readlines()
	outlines = []
	for l in data:
		l = l.strip('\n')
		pieces = l.split(' ')
		if pieces[0]=="Cost:":
			cost = pieces[1]
		elif pieces[0]=="Utterance:":
			utterance = ' '.join(pieces[1:])
		elif pieces[0]=="Evidence:":
			evidences = pieces[1].strip('{').strip('}').split('support')
			probs = evidences[0].strip('"').strip(',').split(':')[1].strip('[').strip(']').split(',')
			worlds = evidences[1].split('}}')[0:-1]
			for i,w in enumerate(worlds):
				pieces = w.split("perspective")
				p = pieces[1].split(':')[-1]
				w = pieces[0].split('world":')[1].strip('"').strip(',').strip('{').strip('}').split(',')
				wanswers = [x.split(':')[1].strip('"') for x in w]
				outlines.append([cost,utterance,p]+wanswers+[probs[i]])
		else:
			pass
	write_results(outlines,sys.argv[2],sys.argv[3])

main()