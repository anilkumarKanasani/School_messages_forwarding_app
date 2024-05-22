# Import necessary libraries
from openai import OpenAI
from environs import Env
import json

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
        model=env("OPEN_AI_MODEL"),  # The model to use
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

def get_open_ai_json(text):
    response = client.chat.completions.create(
        model=env("OPEN_AI_MODEL"),  # The model to use
        messages=[
            {
                "role": "system",  # The role of the message
                "content": """Convert the text into a json object with the following structure:
                {
                    "ID": random 8 digit number,
                    "Date": "5/1/2024",
                    "Description": "Rewe",
                    "Sub-category": "Coupon spendings",
                    "amount": 5,
                    "Location": "Stuttgart",
                    "Mode": "coupons"
                    
                }
                The amount should be a negative number.
                The Sub-category must be from the following list: 
                - Coupon spendings
                - Groceries
                - Restaurant
                - PDP Income
                - Office Travel Income
                - Office Travel Spending
                - PDP Spending
                - To India
                The Mode must be from the following list: 
                - Coupons
                - Creadit_card
                - N26
                If you are not sure, you can use Stuttgart as the location
                """
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
    
    return json.loads(response.choices[0].message.content)