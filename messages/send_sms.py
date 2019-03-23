import os

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get('TWILLO_ACCOUNT_SID')
auth_token = os.environ.get('TWILLO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

sender_phone_number = '+12028497693'
to_phone_number = '+5585999911065'

message = client.messages \
                .create(
                     body="Twillo funciona karaio",
                     from_=sender_phone_number,
                     to=to_phone_number
                 )

print(message.sid)