from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector

with open('../openai.key', 'r') as file:
    code_lines = file.readlines()

for cl in code_lines:
    exec(cl)

embedding_provider = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY
)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://44.201.23.74:7687",
    username="neo4j",
    password="bay-commas-worms",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

result = movie_plot_vector.similarity_search("A movie where aliens land and attack earth.")
for doc in result:
    print(doc.metadata["title"], "-", doc.page_content)