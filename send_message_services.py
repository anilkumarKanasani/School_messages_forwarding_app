# Import necessary libraries
import requests
from environs import Env

# Initialize environment variables
env = Env()
env.read_env("./.env")


def send_telegram_message(msg: str):
    """
    Function to send a Telegram message.

    Parameters:
    msg (str): The message to send.

    Returns:
    None
    """

    TOKEN = env("TELEGRAM_TOKEN")
    chat_id = env("TELEGRAM_CHAT_ID")

    url = (
        f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        f"?chat_id={chat_id}&text={msg}"
    )
    requests.get(url)

    print("!!!!!!!Message sent to telegram!!!!!!!")
