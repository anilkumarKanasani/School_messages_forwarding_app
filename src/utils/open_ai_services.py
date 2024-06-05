# Import necessary libraries
from openai import OpenAI
from environs import Env
import json

# Initialize environment variables
env = Env()
env.read_env("./.env")

# Create an OpenAI client
client = OpenAI()


def get_open_ai_summary(text,content="school"):
    """
    Function to get a summary of the provided text using OpenAI.

    Parameters:
    text (str): The text to summarize.

    Returns:
    str: The summary of the text.
    """
    if content == "school":
        formated_content = """Summarize content you are provided
                            in short and straight in English.
                            It can be as short as possible,
                            but it should provide the complete
                            idea of the content."""
    elif content == "gd":
        formated_content = """You will be provided with the
                            price of gold in the snippet.
                            Extract the price of 22 karats.
                            If not found, return 
                            Failed to extract the price by LLM."""
    # Create a chat completion with the OpenAI API
    response = client.chat.completions.create(
        model=env("OPEN_AI_MODEL"),  # The model to use
        messages=[
            {
                "role": "system",  # The role of the message
                "content": formated_content,
            },
            {
                "role": "user",  # The role of the message
                "content": str(text),  # The content of the message
            },
        ],
        temperature=0,  # The randomness of the output
        max_tokens=4096,  # The maximum number of tokens in the output
        top_p=1,  # The nucleus sampling parameter
    )

    # Return the content of the first choice in the response
    return response.choices[0].message.content