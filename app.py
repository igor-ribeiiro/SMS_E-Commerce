from flask import Flask, request
from messages.sms import SMS
from messages.message import Message
app = Flask(__name__)

sms = SMS()


@app.route("/")
def main():
    return "what's up nigga"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    sent_message = request.form['Body']
    sms_sid = request.form['SmsMessageSid']
    from_number = request.form['From']

    reply_message = f"Replying to your message bitch"

    print_str = f"sent_message = {sent_message}, from_number = {from_number} and sid = {sms_sid}"
    print(print_str)

    reply_message += ', ' + print_str

    return sms.reply_sms(reply_message)

if __name__ == "__main__":
    app.run(debug=True)
