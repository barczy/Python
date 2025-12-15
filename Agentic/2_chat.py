import gradio as gr

from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

system_prompt = """
        Kérlek járj el a nevemben. Barczikay Zsolt vagyok. OTP-ben dolgozom, 49 éves vagyok. 
        Kérlek válaszolj a beérkező kérdésekre a nevemben
"""

client = AzureOpenAI(
        api_key = os.getenv("API_KEY"),
        azure_deployment="gpt-4o",
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version="2024-12-01-preview",
)

def chat(message, history):
    messages=[ {"role": "system", "content": system_prompt }] + history + [{"role": "user", "content": message}]
    print(history)
    response = client.chat.completions.create(messages=messages, max_tokens=4096, temperature=1.0, top_p=1.0, model="gpt-4o",)
    return response.choices[0].message.content

print(chat("Hogy hívnak?",list()))
gr.ChatInterface(chat).launch()


