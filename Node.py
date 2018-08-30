#!/ usr/binenv python
# -*- coding : utf -8 -*-

class Node(object):
	def __init__(self, name, entity, deps=[]):
		self.name = name
		self.entity = entity
		self.deps = deps

	def __repr__(self):
		return self.name + ": " + self.entity
