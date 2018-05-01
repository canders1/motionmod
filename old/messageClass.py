class Message:
	def __init__(self,string,assertions,presuppositions):
		self.utterance = string
		self.assertions = {}
		self.presuppositions = {}
		self.cost = 0.0
		if assertions!=['']:
			for a in assertions:
				self.addAssertion(a.split(","))
		if presuppositions!=['']:
			for p in presuppositions:
				self.addPresupposition(p.split(","))

	def addAssertion(self,a):
		self.assertions[a[0]] = a[1:len(a)]

	def addPresupposition(self,p):
		self.presuppositions[p[0]] = p[1:len(p)]

	def getAssertions(self):
		return self.assertions

	def getPresuppositions(self):
		return self.presuppositions

	def getCost(self):
		return self.cost

	def getUtterance(self):
		return self.utterance

	def __str__(self):
		if self.assertions == {}:
			assertString = "None"
		else:
			assertString = ""
			for pred in self.assertions.keys():
				assertString += pred+" "+" ".join(self.assertions[pred])
		if self.presuppositions =={}:
			presupString = "None"
		else:
			presupString = " "
			for pred in self.presuppositions.keys():
				presupString += pred+" "+" ".join(self.presuppositions[pred])
		return self.utterance+": assertions {"+assertString+"}, presuppositions {"+presupString+"}"