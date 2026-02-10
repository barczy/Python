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
    is_name_in_message: bool
    name: str


guardrail_agent = Agent(name='Name check', instructions='Check is there a name in the user message', 
                        output_type = NameCheckOutput, model=azure_model)

@input_guardrail(run_in_parallel=True)
async def guardrail_against_name(ctx, agent, input):
    result=await Runner.run(guardrail_agent, input, context=ctx.context)
    is_name_in_message = result.final_output.is_name_in_message
    print(is_name_in_message)
    return GuardrailFunctionOutput(output_info={"found name": result.final_output}, tripwire_triggered=is_name_in_message)

agent = Agent(name='Azure teszt', instructions='Én egy banki asszisztens vagyok!', 
              input_guardrails=[guardrail_against_name], model=azure_model)

async def main():
    result = await Runner.run(agent, "Please greet someone!" )
    ## result = await Runner.run(agent, "Please greet Tom!" ) ## ez Guardrail exception-t fog dobni, mert van benne név!
    print(result.final_output)

asyncio.run(main())
