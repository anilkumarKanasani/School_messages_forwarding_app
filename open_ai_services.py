# Import necessary libraries
from openai import OpenAI
from environs import Env

# Initialize environment variables
env = Env()
env.read_env("./.env")

# Create an OpenAI client
client = OpenAI()


def get_open_ai_summary(text):
    """
    Function to get a summary of the provided text using OpenAI.

    Parameters:
    text (str): The text to summarize.

    Returns:
    str: The summary of the text.
    """
    # Create a chat completion with the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",  # The model to use
        messages=[
            {
                "role": "system",  # The role of the message
                "content": """Summarize content you are provided
                            in short and straight in English.
                            It can be as short as possible,
                            but it should provide the complete
                            idea of the content.""",
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
