import os
from openai import OpenAI
from environs import Env
env = Env()
env.read_env("./.env")

client = OpenAI()

def get_open_ai_summary(text):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {
        "role": "system",
        "content": "Summarize content you are provided in short and stright in english. It can be as short as possible, but it should provide the complete idea of the content."
        },
        {
        "role": "user",
        "content": str(text)
        }
    ],
    temperature=0,
    max_tokens=4096,
    top_p=1
    )
    return response.choices[0].message.content