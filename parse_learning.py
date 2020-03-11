import sys

def write_results(outlines,outputfile):
	with open(outputfile,'w') as wf:
		for l in outlines:
			print(l)
			wf.write('\t'.join(l)+'\n')
	return

def parse_dist(d):
	return d.split(',')

def parse_w(w):
	pieces = w.strip('{').strip('}').split(',')
	world = [p.split(':')[1].strip(' ').strip('\"') for p in pieces]
	return world

def w_string(world):
	words = [w.split(' ')[0] for w in world]
	return '_'.join(words)

def main():
	if len(sys.argv) < 4:
		print("Usage: python parse_learning.py inputfile worldfile outputfile")
		return

	wf = open(sys.argv[2],'r').readlines()
	worlds = [parse_w(w.strip('\n')) for w in wf]
	data = open(sys.argv[1],'r').readlines()
	outlines = []
	for l in data:
		l = l.strip('\n')
		pieces = l.split(' ')
		if pieces[0]=="Gen":
			gen = pieces[1]
		elif pieces[0]=="Observed:":
			obs_w = parse_w(' '.join(pieces[1:]))
		elif pieces[0]=="Uttered:":
			utt = ' '.join(pieces[1:]).strip('\"')
		elif pieces[0]=="Interpretation:":
			inter = pieces[1]
		elif pieces[0] == "Speaker":
			speakPost = pieces[2]
		elif pieces[0] == "Listener":
			listPost = pieces[2]
			speakPosts = parse_dist(speakPost)
			listPosts = parse_dist(listPost)
			for i,w in enumerate(worlds):
				outlines.append([gen]+obs_w+[w_string(obs_w),utt]+w+[w_string(w),'speaker',speakPosts[i]])
				outlines.append([gen]+obs_w+[w_string(obs_w),utt]+w+[w_string(w),'listener',listPosts[i]])
		else:
			pass
	write_results(outlines,sys.argv[3])

main()