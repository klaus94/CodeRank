#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
import sys
from Node import *
from Neo4j import *

# check, if matched key-word is part of a string in this line
def isPartOfString(lineSplit, idx):
	stringOpen = False
	for i, word in enumerate(lineSplit):
		if i == idx:
			return stringOpen
		if "\"" in word or "'" in word or "`" in word:
			stringOpen = not stringOpen


def findEntityName(filePath):
	myFile = open(filePath, 'r')
	# replace characters that could follow after a class-name, e.g. class Person{} or class Person(object)
	content = myFile.read().replace("(", " ").replace("{", " ").replace("<", " ")
	lines = content.split("\n")
	myFile.close()
	isInComment = False
	for line in lines:
		if line.strip().startswith("//"):		# todo: add more comment-signs
			continue

		# handle multiline-comments
		if line.strip().startswith("/*"):
			isInComment = True
			continue
		if isInComment and "*/" in line:
			isInComment = False
			continue
		if isInComment:
			continue

		split = line.split(" ")
		try:
			idx = split.index("class")			# todo: add more keywords here (interface, enum, ...)
												# or think of solution for configs for different languages
			if len(split) > idx and not isPartOfString(split, idx):
				# if split[idx+1] == "as":
				# 	print "found: " + split[idx+1] + " is not part of string: " + str(split)
				return split[idx+1]
		except ValueError as e:
			pass

	return None

# get all files with their filename and path
rootDir = "."
if len(sys.argv) > 1:
	rootDir = sys.argv[1]
allFilePaths = []
for root, _, filenames in os.walk(rootDir):
	for fileName in filenames:
		allFilePaths.append(root + "/" + fileName)

# find entities and initialize nodes
nodes = {}
entities = []
for path in allFilePaths:
	entity = findEntityName(path)
	if entity is None:
		continue
	entities.append(entity)
	nodes[entity] = Node(entity, path)			# maybe datastructure could be better (entry is stored twice)

# print entities
# print nodes

# fill dependencies of nodes
for node in nodes.values():
	for possibleDepNode in nodes.values():
		if node == possibleDepNode:
			continue
		myFile = open(possibleDepNode.filePath, 'r')
		if node.name in myFile.read():
			possibleDepNode.deps.append(node.name)
		myFile.close()

# print nodes
graphClear()
buildGraph(nodes)

# for key, value in nodes.items():
# 	print key
# 	if key == "as":
# 		print "here comes the if:"
# 		print value
# 	print "...."