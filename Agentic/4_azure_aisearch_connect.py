"""
Szöveg vektorizálása majd feltöltése AI Search vektor adatbázisba
"""
import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)

## szöveg vektorizálása
embeddings = AzureOpenAIEmbeddings(
    azure_endpoint = os.getenv("EMBEDDING_AZURE_ENDPOINT"),
    azure_deployment = os.getenv("EMBEDDING_AZURE_DEPLOYMENT"),
    openai_api_version = os.getenv("EMBEDDING_OPENAI_API_VERSION"),
    model = os.getenv("EMBEDDING_MODEL"),
    api_key = os.getenv("EMBEDDING_API_KEY"),
)

doc_text = "OpenAI is an AI research and deployment company aiming to build safe, beneficial Artificial General Intelligence (AGI) for humanity"
vector = embeddings.embed_query(doc_text)
print(vector)

## Vektorizált dokumentum feltöltésének előkészítése
document = {
    "id": "1",
    "content": doc_text,
    "contentVector": vector
}

## AI Search kapcsolat, meglévő index használata
search_client = SearchClient(
        endpoint = os.getenv("AISEARCH_AZURE_ENDPOINT"),
        index_name="chat_assistant_description",
        credential=AzureKeyCredential(os.getenv("AISEARCH_API_KEY"))
)
## Upload to Azure Search
result = search_client.upload_documents(documents=[document])
print("Upload result:", result)