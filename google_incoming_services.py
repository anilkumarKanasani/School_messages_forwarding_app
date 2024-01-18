import os.path
import json
import base64
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from environs import Env
env = Env()
env.read_env("./.env")


# If modifying these scopes, delete the file token.json.
SCOPES = [
            "https://www.googleapis.com/auth/gmail.readonly"
        ]

def get_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    service = build("gmail", "v1", credentials=creds)

    return service

def get_all_messages(service):
    try:
        results = (
                    service.users()
                    .messages()
                    .list(userId="me", labelIds=["INBOX"])
                    .execute()
                )
        
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
            return None

        else:
            return messages

    except HttpError as error:
        print("An error occurred: %s" % error)

def get_message_body(service, messages):
        try:
            all_messages = []
            for message in messages:
                msg = (
                        service.users()
                        .messages()
                        .get(userId="me", id=message["id"])
                        .execute()
                )
                if any(s in json.dumps(msg) for s in [env("SCHOOL_ADDRESS_1"), env("SCHOOL_ADDRESS_2")]):
                    payload = msg['payload']
                    data = payload['parts'][0]['body']['data']
                    data = data.replace("-","+").replace("_","/")
                    decoded_data = base64.b64decode(data)
                    soup = BeautifulSoup(decoded_data , "lxml")
                    body = soup.body()
                    all_messages.append(body)
            return all_messages
    
        except HttpError as error:
            print("An error occurred: %s" % error)


