# Call AzureOpenAI with the OpenAI package
# saraijoe tennant
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)

## azaz llm válaszában fellelhető a tool, aminek a hívását kéri, ezt mi tesszük meg manuálisan
def handle_tool_calls(tool_calls):
    for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool calles: {tool_name}", flush=True)
            if tool_name=="greeting":
                greeting(**arguments)


## ez lesz egy meghívható tool
def greeting(person_name) :
    print(f"Hello {person_name}!")

## ez lesz a tool leírója, amit az LLM megkap
greeting_json = {
    "name": "greeting",
    "description": "Always use this tool to greet somebody",
    "parameters" : {
            "type" : "object",
            "properties" : {
                "person_name" : {
                    "type": "string",
                    "description": "The name you want to greet"
                }
            }
        }
}
tools = [{"type": "function", "function": greeting_json }]

## system promptban utalunk a tool-ra
system_prompt = f"A bejövő üznetben találd meg az illető nevét. \
    Ha megtaláltad az illető nevét, akkor a megfelelő tool meghívásával üdvözöld őt."
message = "Szia! Én Tamás vagyok, örülök, hogy beszélhetek veled!"

client = AzureOpenAI(
        api_key = os.getenv("API_KEY"),
        azure_deployment="gpt-4o",
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version="2024-12-01-preview",
)

messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]

## a hívásban átadjuk a tool objektumot!!!!!
response = client.chat.completions.create(messages=messages, tools = tools, model="gpt-4o")

### a válaszban feltűnik a tool_calls reason és a tool_calls objektum!
print(response.choices[0])
print("-----")
if response.choices[0].finish_reason=="tool_calls":
    handle_tool_calls(response.choices[0].message.tool_calls)


