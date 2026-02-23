from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
from agents.mcp import MCPServerStdio
import asyncio
import os
from openai import AsyncOpenAI


load_dotenv(override=True)

azure_client = AsyncOpenAI(base_url=os.getenv("API_ENDPOINT") , api_key=os.getenv("API_KEY"))
azure_model = OpenAIChatCompletionsModel(model='gpt-4o', openai_client=azure_client)


fetch_params = {"command": "uvx", "args" : ["mcp-server-fetch"]}  # futtat egy uv pythont és egy python repo nevet...

async def main():
    async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=30) as server:
        fetch_tools = await server.list_tools()
        print(fetch_tools)

asyncio.run(main())
