#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
import sys
from Node import *

def findEntityName(filePath):
	myFile = open(filePath, 'r')
	# replace characters that could follow after a class-name, e.g. class Person{} or class Person(object)
	content = myFile.read().replace("\n", " ").replace("(", " ").replace("{", " ")
	myFile.close()
	split = content.split(" ")
	print split
	try:
		idx = split.index("class")			# todo: add more keywords here
		if len(split) > idx:
			return split[idx+1]
	except ValueError as e:
		pass

	return ""
	

def createNodes(fileNames, filePaths):
	global nodes
	for name, path in zip(fileNames, filePaths):
		entity = findEntityName(path)
		nodes.append(Node(name, entity))


rootDir = "."
if len(sys.argv) > 1:
	rootDir = sys.argv[1]

allFileNames = []
allFilePaths = []
for root, _, filenames in os.walk(rootDir):
	for fileName in filenames:
		allFileNames.append(fileName)
		allFilePaths.append(root + "/" + fileName)

nodes = []
createNodes(allFileNames, allFilePaths)
print nodes
