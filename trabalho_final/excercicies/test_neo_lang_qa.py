from langchain_openai import ChatOpenAI
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain.prompts import PromptTemplate

from load_variables import OPENAI_API_KEY, NEO4J_URL, NEO4J_USERNAME, NEO4J_PASSWORD

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY
)

graph = Neo4jGraph(
    url=NEO4J_URL,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD
)

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.

Schema: {schema}
Question: {question}
"""

cypher_generation_prompt = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"],
)

cypher_chain = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    cypher_prompt=cypher_generation_prompt,
    verbose=True
)

#cypher_chain.invoke({"query": "What role did Tom Hanks play in Toy Story?"})
cypher_chain.invoke({"query": "How many movies has Tom Hanks directed?"})