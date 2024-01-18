from google_incoming_services import get_service, get_all_messages, get_message_body
from open_ai_services import get_open_ai_summary
from send_message_services import send_whatsapp_message

if __name__ == "__main__":
    service = get_service()
    messages = get_all_messages(service)
    
    if messages is not None:
        message_bodies = get_message_body(service, messages)
        for body in message_bodies:
            summary = get_open_ai_summary(body)
            send_whatsapp_message(msg=summary)
            

        print("All messages translated and sent!")