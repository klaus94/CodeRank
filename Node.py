#!/ usr/binenv python
# -*- coding : utf -8 -*-

class Node(object):
	def __init__(self, name, filePath):
		self.name = name
		self.filePath = filePath
		self.deps = []

	def __repr__(self):
		return self.name + " (" + self.filePath + ") : " + str(self.deps)

	def __eq__(self, other):
		return self.name == other.name

	def __ne__(self, other):
		return not self.__eq__(other)