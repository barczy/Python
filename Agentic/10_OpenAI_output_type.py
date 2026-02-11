from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import asyncio
import os
from openai import AsyncOpenAI
from pydantic import BaseModel
from agents import input_guardrail, GuardrailFunctionOutput

load_dotenv(override=True)

azure_client = AsyncOpenAI(base_url=os.getenv("API_ENDPOINT") , api_key=os.getenv("API_KEY"))
azure_model = OpenAIChatCompletionsModel(model='gpt-4o', openai_client=azure_client)


class NameCheckOutput(BaseModel):
    name: str
    birthday: str
    famousfor: str


agent = Agent(name='Azure teszt', instructions='I need personal information about famous people. The whole name, the date of birth' \
            ' and a short description, what is he or she famous for.', 
              output_type=NameCheckOutput, model=azure_model)

async def main():
    result = await Runner.run(agent, "I need information about John Lennon!" )
    print(result.final_output.birthday)
    print(result.final_output.famousfor)

asyncio.run(main())
