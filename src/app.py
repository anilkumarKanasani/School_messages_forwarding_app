
from utils.send_message_services import send_telegram_message


import os
import ast
app_mode = os.getenv("app_mode")

# Main execution
if __name__ == "__main__":
    if app_mode == "gold_app":
        from gold_app.gold_app import get_gold_price
        from utils.open_ai_services import get_open_ai_summary
        gold_price = get_gold_price()
        message = get_open_ai_summary(gold_price, content="gd")
        send_telegram_message(msg=message, backup=True)
        print("Gd message sent!")

    elif app_mode == "exp_tracking_app":
        from exp_tracking_app.all_exp_messages import get_all_messages
        from utils.send_message_services import enter_gsheet_message

        messages = get_all_messages()
        
        for message in messages:
            try:
                mess_dict = ast.literal_eval(message.strip('"'))
                mess_dict["amount"] = float(mess_dict["amount"])
            except:
                print(message +  " Error in converting to JSON.")
                mess_dict = {}

            
            enter_gsheet_message(db_name = "Expenses_app_db", new_row= mess_dict)

        # Print a success message
        print(str(len(messages)) + "  expenses entered into gsheets!")            

    elif app_mode == "school_app":
        from school_app.google_incoming_services import (
                        get_service,
                        get_all_messages,
                        get_message_body,
                        )
        from utils.open_ai_services import get_open_ai_summary
        # Get the Google service
        service = get_service()

        # Get all messages from the service
        messages = get_all_messages(service)

        # Check if there is no new messages from school
        if messages is None:
            print("No messages from school found today.")

        else:
            # Get the body of each message
            message_bodies = get_message_body(service, messages)

            if len(message_bodies) == 0:
                # If no messages are found, print a message and return None
                print("No messages from school found today.")

            # Loop through each message body
            for body in message_bodies:
                # Get the summary of the message body using OpenAI
                try:
                    summary = get_open_ai_summary(body, content="school")
                except:
                    summary = body

                # Send the summary as a Telegram message
                send_telegram_message(msg=summary, backup=False)

            # Print a success message
            print("All messages translated and sent!")