#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
import sys
from Node import *
from Neo4j import *

def findEntityName(filePath):
	myFile = open(filePath, 'r')
	# replace characters that could follow after a class-name, e.g. class Person{} or class Person(object)
	content = myFile.read().replace("\n", " ").replace("(", " ").replace("{", " ")
	myFile.close()
	split = content.split(" ")
	try:
		idx = split.index("class")			# todo: add more keywords here (interface, enum, ...)
											# or think of solution for configs for different languages
		if len(split) > idx:
			return split[idx+1]
	except ValueError as e:
		pass

	return None

# get all files with their filename and path
rootDir = "."
if len(sys.argv) > 1:
	rootDir = sys.argv[1]
allFileNames = []
allFilePaths = []
for root, _, filenames in os.walk(rootDir):
	for fileName in filenames:
		allFileNames.append(fileName)
		allFilePaths.append(root + "/" + fileName)

# find entities and initialize nodes
nodes = {}
entities = []
for name, path in zip(allFileNames, allFilePaths):
	entity = findEntityName(path)
	if entity is None:
		continue
	entities.append(entity)
	nodes[entity] = Node(name, entity, path)			# maybe datastructure could be better (entry is stored twice)

# print entities
# print nodes

# fill dependencies of nodes
for node in nodes.values():
	for possibleDepNode in nodes.values():
		if node == possibleDepNode:
			continue
		myFile = open(possibleDepNode.filePath, 'r')
		if node.entity in myFile.read():
			possibleDepNode.deps.append(node.entity)
		myFile.close()

# print nodes
graphClear()
buildGraph(nodes)