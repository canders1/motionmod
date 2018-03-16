class World:
	def __init__(self,name,entities):
		self.name = name
		if entities == {}:
			self.entities = {'entity':[]}
		else:
			self.entities = entities
		self.propositions = {}

	def addProposition(self,prop):
		pred = prop[0]
		entities = prop[1:len(prop)]
		for e in entities:
			if e not in self.entities["entity"]:
				entry = self.entities["entity"]
				entry.append(e)
				self.entities["entity"] = entry
		if pred in self.propositions:
			entry = self.propositions[pred]
			entry.append(entities)
			self.propositions[pred] = entry
		else:
			self.propositions[pred] = [entities]

	def checkProposition(self,prop):
		pred = prop[0]
		entities = prop[1:len(prop)]
		if pred not in self.propositions:
			print "Warning: predicate is undefined!"
			return
		else:
			entry = self.propositions[pred]
			if entities in entry:
				return True
			else:
				return False

	def getPropositions(self):
		return self.propositions

	def getDefinedEntities(self):
		return self.entities["entity"]

	def getName(self):
		return self.name

w = World("w1")
w.addProposition(["exists","Sarah"])
w.addProposition(["exists","I"])
w.addProposition(["exists","you"])
w.addProposition(["eats","Sarah","apple"])
print w.entities
print w.propositions
print w.checkProposition(["exists","Sarah"])
print w.checkProposition(["exists","Jill"])
print w.checkProposition(["lives","Jill"])


