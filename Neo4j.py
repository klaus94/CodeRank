#!/ usr/binenv python
# -*- coding : utf -8 -*-

from py2neo import Graph

def test():
	graph = Graph("http://neo4j:123456@localhost:7474")
	a = graph.run("CREATE (person:Person {name:'Alice1'}) RETURN person")
	print a