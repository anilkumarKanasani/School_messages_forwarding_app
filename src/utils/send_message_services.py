# Import necessary libraries
import requests
from environs import Env

# Initialize environment variables
env = Env()
env.read_env("./.env")


def send_telegram_message(msg: str, backup: bool):
    """
    Function to send a Telegram message.

    Parameters:
    msg (str): The message to send.
    backup (bool): redirect to backup chat or not.

    Returns:
    None
    """

    if backup:
        TOKEN = env("BKP_TELEGRAM_TOKEN")
        chat_id = env("BKP_TELEGRAM_CHAT_ID")
    else:
        TOKEN = env("TELEGRAM_TOKEN")
        chat_id = env("TELEGRAM_CHAT_ID")
    
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(TOKEN, "sendMessage"),
        data={'chat_id': chat_id, 'text': msg}
            ).json()
    
    if response['ok']:
        print("!!!!!!!Message sent to telegram!!!!!!!")
    else:
        print(response)
