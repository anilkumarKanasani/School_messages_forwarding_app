# School_messages_forwarding_app
This is a simple app that forwards messages from a school's communcation emails to a telegram channel. It is written in python and uses Google API to scrape the emails, openAI to summarize the content and  telethon to send or receive messages to the Telegram channel. It is currently configured to work with the Emails from the school which has specific endings from environment varaibles. But it can be easily modified to work with any other website.

## Installation
To install the app, you need to have python 3.11 or higher installed on your computer. You also need to install the packages from requirements.txt. You can do this by running the following command in the terminal:
```
pip install -r requirements.txt
```

## Configuration
To configure the app, you need to create a file called token.json and gsheet_credentials.json in the same directory as the app.py file. In this file, you need to define the variables connecting to Google API.

## Environment variables
The app uses environment variables to store sensitive data. You need to create a file called .env in the same directory as the app.py file. In this file, you need to define the following variables:
```
SCHOOL_ADDRESS_1 = <your school email address ending> ex: @zphs.com
SCHOOL_ADDRESS_2 = <your school email address ending> ex: @loyola.com
OPENAI_API_KEY = <your open AI api id>

TELEGRAM_TOKEN = <your telegram bot token>
TELEGRAM_CHAT_ID = <your telegram chat id>
```

## Running the app
To run the app, you need to run the following command in the terminal:
```
python app.py 
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
