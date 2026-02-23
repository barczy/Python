'''
With MCP szervers, the Agents will access the internet, will search info, and save it to local disk
'''

from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
from agents.mcp import MCPServerStdio
import asyncio
import os
from openai import AsyncOpenAI


load_dotenv(override=True)

azure_client = AsyncOpenAI(base_url=os.getenv("API_ENDPOINT") , api_key=os.getenv("API_KEY"))
azure_model = OpenAIChatCompletionsModel(model='gpt-4o', openai_client=azure_client)

# playwright is a microsoft based MCP szerver, browser
# ez egy javascript alapú, node package manager (npx). Node.JS
playwright_params = {"command": "npx", "args": ["@playwright/mcp@latest"]} 
sandbox_path = os.path.abspath(os.path.join(os.getcwd(),"sandbox"))

# ez egy olyan, ami a fájlrendszeremből fog tudni olvasni és írni
sandbox_path = "/Users/zsoltbarczikay/Documents/TMP/"
files_params = {"command": "npx", "args": ["-y" , "@modelcontextprotocol/server-filesystem", sandbox_path]} 

instructions = "You can browse the internet to accomplish instructions!"

async def main():
    async with MCPServerStdio(params=files_params, client_session_timeout_seconds=30) as mcp_server_files:
        async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=30) as mcp_server_browse:

            # agent, ami az MCP toolokat használni fogja
            agent = Agent(
                name = "investigator",
                instructions = instructions,
                mcp_servers= [mcp_server_files, mcp_server_browse],
                model = azure_model
            )

            # kilistázza a tool funkcióit
            playwright_tools = await mcp_server_files.list_tools()
            print(playwright_tools)

            result = await Runner.run(agent, "Find the most relevant news about Washington, \
                                      and summerize it in markdown to news.md and save it to localdisk through MCP tools!")
            print(result.final_output)


asyncio.run(main())
