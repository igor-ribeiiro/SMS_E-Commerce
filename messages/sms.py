import os

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


class SMS:
    def __init__(self):
        account_sid = os.environ.get('TWILLO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILLO_AUTH_TOKEN')
        self.client = Client(account_sid, auth_token)
        self.sender_phone_number = '+12028497693'

    def send_sms(self, to_phone_number, message):
        message = self.client.messages \
                        .create(
                            body=message,
                            from_=self.sender_phone_number,
                            to=to_phone_number
                        )

        print(message.sid)

    def reply_sms(self, message):
        resp = MessagingResponse()
        resp.message(message)

        return str(resp)

if __name__ == "__main__":
    to_phone_number = '+5585999911065'
    message = "Twillo funciona karaio"

    sms = SMS()
    sms.send_sms(to_phone_number, message)
