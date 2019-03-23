from flask import Flask, request
from messages.sms import SMS
app = Flask(__name__)

sms = SMS()


@app.route("/")
def main():
    return "what's up nigga"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    sent_message = request.form['Body']
    from_number = request.form['From']

    reply_message = f"Replying to your message bitch"

    print_str = f"sent_message = {sent_message} and from_number = {from_number}"
    print(print_str)

    reply_message += ', ' + print_str

    return sms.reply_sms(reply_message)

if __name__ == "__main__":
    app.run(debug=True)
