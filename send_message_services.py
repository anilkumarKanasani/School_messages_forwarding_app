import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
from environs import Env
env = Env()
env.read_env("./.env")

keyboard = Controller()

def send_whatsapp_message(msg: str):
    try:
        print(msg)
        pywhatkit.sendwhatmsg_instantly(
            phone_no=env("Phone_number"), 
            message=msg,
            tab_close=True
        )
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("!!!!!!!Message sent!!!!!!!")
        input("Press Enter to continue...")
    except Exception as e:
        print(str(e))
