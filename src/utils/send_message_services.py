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
        TOKEN = env("BKP_TELEGRAM_TOKEN").replace('"', "")
        chat_id = env("BKP_TELEGRAM_CHAT_ID").replace('"', "")
    else:
        TOKEN = env("TELEGRAM_TOKEN").replace('"', "")
        chat_id = env("TELEGRAM_CHAT_ID").replace('"', "")
    
    url = (
        f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        f"?chat_id={chat_id}&text={msg}"
    )

    response = requests.get(url)

    
    if response.json()['ok']:
        print("!!!!!!!Message sent to telegram!!!!!!!")
    else:
        print(response)

def enter_gsheet_message(db_name: str, new_row: dict):
    import gspread
    gc = gspread.service_account(filename="./gsheet_credentials.json")
    wk_sht = gc.open(db_name)
    # add new row to wk_sht
    wk_sht.worksheet("Writing_table").append_row(list(new_row.values()))
