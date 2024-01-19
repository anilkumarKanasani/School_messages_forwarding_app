# Import necessary libraries
import time
import requests
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
from environs import Env

# Initialize environment variables
env = Env()
env.read_env("./.env")

# Initialize a Controller object from pynput.keyboard
keyboard = Controller()

def send_whatsapp_message(msg: str):
    """
    Function to send a WhatsApp message.

    Parameters:
    msg (str): The message to send.

    Returns:
    None
    """
    try:
        # Send the WhatsApp message instantly
        pywhatkit.sendwhatmsg_instantly(
            phone_no=env("Phone_number"),  # The phone number to send the message to
            message=msg,  # The message to send
            tab_close=True  # Close the tab after sending the message
        )

        # Wait for 2 seconds
        time.sleep(2)

        # Click the current position
        pyautogui.click()

        # Wait for 2 seconds
        time.sleep(2)

        # Press and release the Enter key
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        # Print a success message
        print("!!!!!!!Message sent!!!!!!!")

        # Wait for the user to press Enter to continue
        input("Press Enter to continue...")

    except Exception as e:
        # If an exception occurs, print the exception
        print(str(e))


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

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    response = requests.get(url)

    print("!!!!!!!Message sent to telegram!!!!!!!")