import datetime
from environs import Env
from telethon import TelegramClient

# Initialize environment variables
env = Env()
env.read_env("./.env")

def get_all_messages():
    telgm_client = TelegramClient('anil_telegram', env("TELEGRAM_APP_ID"), env("TELEGRAM_API_HASH"))
    telgm_client.start(phone=env("TELEGRAM_PHONE"))

    yesterday = datetime.datetime.today()# - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%m/%d/%Y")

    all_messages = []
    # Connect to the client asynchronously
    with telgm_client:
        for message in telgm_client.iter_messages(None, limit=100):
            try:
                if message.peer_id.user_id==6876932398 and message.text!=None and message.date.strftime("%m/%d/%Y")==yesterday:
                    all_messages.append(yesterday + " " + message.text)
                    
            except:
                pass
    return all_messages