from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
from agents.mcp import MCPServerStdio
import asyncio
import os
from openai import AsyncOpenAI


load_dotenv(override=True)
azure_client = AsyncOpenAI(base_url=os.getenv("API_ENDPOINT") , api_key=os.getenv("API_KEY"))
azure_model = OpenAIChatCompletionsModel(model='gpt-4o', openai_client=azure_client)


my_mcp_params = {"command": "uv", "args" : ["run", "/Users/zsoltbarczikay/dev/Python/Agentic/13_OpenAI_MCP_server.py"]}  # futtat egy uv pythont és egy python repo nevet...
instructions = "You have to use the MCP server, you have got, for greeting Tom! You must use the output word by word! "

async def main():
    async with MCPServerStdio(params=my_mcp_params, client_session_timeout_seconds=30) as my_mcp_server:
        my_mcp_tools = await my_mcp_server.list_tools()
        print(my_mcp_tools)
    
                    # agent, ami az MCP toolokat használni fogja
        agent = Agent(
                name = "greeting",
                instructions = instructions,
                mcp_servers= [my_mcp_server],
                model = azure_model
            )


        result = await Runner.run(agent, instructions)
        print(result.final_output)

asyncio.run(main())