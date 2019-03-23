from flask import Flask, request
from sms import SMS

app = Flask(__name__)

sms = SMS()

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    message = "Reply message test"

    return sms.reply_sms(message)


if __name__ == "__main__":
    app.run(debug=True)
