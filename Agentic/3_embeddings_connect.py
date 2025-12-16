import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv(override=True)

azure_endpoint = os.getenv("EMBEDDING_AZURE_ENDPOINT")
azure_deployment= os.getenv("EMBEDDING_AZURE_DEPLOYMENT")
openai_api_version = os.getenv("EMBEDDING_OPENAI_API_VERSION")
model = os.getenv("EMBEDDING_MODEL")
api_key = os.getenv("EMBEDDING_API_KEY")

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint = azure_endpoint,
    azure_deployment = azure_deployment,
    openai_api_version = openai_api_version,
    model = model,
    api_key = api_key,
  
)
print(embeddings.embed_query("Hello, what is the capital of France?"))