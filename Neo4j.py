#!/ usr/binenv python
# -*- coding : utf -8 -*-

from py2neo import Graph

graph = Graph("http://neo4j:123456@localhost:7474")

def graphClear():
	graph.run("MATCH (n:Node) DETACH DELETE n")

def drawEdge(nodeFrom, nodeTo):
	graph.run("MATCH (nFrom:Node {name: '" + nodeFrom + "'}), (nTo:Node {name: '" + nodeTo + "'}) CREATE (nFrom)-[r:DEP]->(nTo)")

def buildGraph(nodesDict):
	for node in nodesDict.values():
		graph.run("CREATE (n:Node {name:'" + node.name + "', path:'" + node.filePath + "'}) RETURN n")
		for depNode in node.deps:
			drawEdge(node.name, depNode)