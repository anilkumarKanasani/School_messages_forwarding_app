
from utils.send_message_services import send_telegram_message


import os
app_mode = os.getenv("app_mode")

# Main execution
if __name__ == "__main__":
    if app_mode == "gold_app":
        from gold_app.gold_app import get_gold_price
        gold_price = get_gold_price()
        send_telegram_message(msg=gold_price, backup=True)
        print("Gd message sent!")

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
                    summary = get_open_ai_summary(body)
                except:
                    summary = body

                # Send the summary as a Telegram message
                send_telegram_message(msg=summary, backup=False)

            # Print a success message
            print("All messages translated and sent!")