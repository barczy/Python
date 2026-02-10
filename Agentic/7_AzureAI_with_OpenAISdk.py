from agents import Agent, Runner, trace, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import asyncio
import os
from openai import AsyncOpenAI

load_dotenv(override=True)

azure_client = AsyncOpenAI(base_url=os.getenv("API_ENDPOINT") , api_key=os.getenv("API_KEY"))
azure_model = OpenAIChatCompletionsModel(model='gpt-4o', openai_client=azure_client)
agent = Agent(name='Azure teszt', instructions='Én egy banki asszisztens vagyok!' ,model=azure_model)

async def main():
    result = await Runner.run(agent, "Tell a joke!")
    print(result.final_output)

asyncio.run(main())
