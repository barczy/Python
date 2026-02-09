## python3 -m pip install agent-framework-azure-ai
import asyncio
from dotenv import load_dotenv
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import ChatAgent
import os

load_dotenv(override=True)

chat_client = AzureOpenAIChatClient(
        api_key = os.getenv("API_KEY"),
        deployment_name="gpt-4o",
        endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version="2024-12-01-preview",
)
agent = ChatAgent(name="Jokester", instructions="You are a bank assistent.", chat_client=chat_client)

async def main():
    result = await agent.run("Tell a joke!")
    print(result)

asyncio.run(main())