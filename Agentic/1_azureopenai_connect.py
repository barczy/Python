# Call AzureOpenAI with the OpenAI package
# saraijoe tennant
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def call_AzureOpenAI():
    """
    Call AzureOpenAI with the OpenAI package
    """

    client = AzureOpenAI(
        api_key = os.getenv("API_KEY"),
        azure_deployment="gpt-4o",
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version="2024-12-01-preview",
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Hello, what is the capital of France?"
            }
        ],
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
        model="gpt-4o",
        )
    print(response.choices[0].message.content)

if __name__== "__main__":
    call_AzureOpenAI()