from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="bolt://44.201.23.74:7687",
    username="neo4j",
    password="bay-commas-worms"
)

result = graph.query("""
MATCH (m:Movie{title: 'Toy Story'}) 
RETURN m.title, m.plot, m.poster
""")

print(result)

print(graph.schema)