from llama_index.core import SummaryIndex
from llama_index.readers.mongodb import SimpleMongoReader
from llama_index.llms.openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

host = os.getenv("MONGO_URL")
port = 27017
db_name = os.getenv("MONGO_DB_NAME")
collection_name = "Products"

query_dict = {}
field_names = []

reader = SimpleMongoReader(host, port)
documents = reader.load_data(
    db_name, collection_name, field_names, query_dict=query_dict
)

index = SummaryIndex.from_documents(documents)

query_engine = index.as_query_engine(llm=llm)

while True:
    query = input("Enter your query: ")
    response = query_engine.query(query)

    print(response)
