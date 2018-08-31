# Coderank

**Problem:** Große Softwareprojekte sind oft unübersichtlich und ein Einstieg fällt oft schwer. Auch Dokumentationen helfen selten bei einem schnellen Einstieg, da sie meist zu ausführlich sind und keinen Fokus auf die wesentlichen Teile der Software legen (z.b. Javadoc). Eine Dokumentation mithilfe von UML durch den Entwickler wäre wünschenswert, aber ist sehr aufwändig und ist schnell nicht mehr up-to-date.

**Ziel**: Mit Coderank soll es möglich sein, Code statisch zu analysieren. Dazu sollen die Abhängigkeiten zwischen Dateien / Klassen in Form eines Graphen dargestellt werden. Auf dem Graphen soll dann der PageRank-Algorithmus angewendet werden. Dadurch sollen besonders wichtige Dateien / Klassen ermittelt werden. Schön wäre noch eine graphische Darstellung des Ergebnisses.



**Technologien:**

- Python
- neo4j
- neo4j-Plugin Algo (https://github.com/neo4j-contrib/neo4j-graph-algorithms)
- Graphik-Bibliothek ???



Related work: https://ieeexplore.ieee.org/document/7208254/



Ablauf:

- neo4j starten (gegebenenfalls User und Passwort in Neo4j.py ändern)

> \> python Reader.py [projectDirToAnalyse]

- erzeugt neo4j-Graph von Entitäten im Projekt:
  - Knoten (Node): Name der Entität
  - Kante (DEP): verweist auf andere Knoten, zu denen eine Abhängigkeit besteht

- Mithilfe des Pagerank-Algorithmus können pagerank-Werte der einzelnen Knoten geschrieben werden. Dazu folgenden Befehl auf neo4j-Graph abfeuern:

> \> CALL algo.pageRank('Node', 'DEP', {iterations:5, dampingFactor:0.85, write: true, writeProperty:'pagerank', concurrency:4})



TODO:

- automatisches Starten der Pagerank-Berechnung
- Auswertung der Pagerank-Werte (evt mit graphischer Darstellung)