#!/ usr/binenv python
# -*- coding : utf -8 -*-

class Node(object):
	def __init__(self, name, entity, filePath):
		self.name = name
		self.entity = entity
		self.filePath = filePath
		self.deps = []

	def __repr__(self):
		return self.name + ": " + self.entity + " " + str(self.deps)

	def __eq__(self, other):
		return self.name == other.name

	def __ne__(self, other):
		return not self.__eq__(other)