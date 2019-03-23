from flask import Flask, request
app = Flask(__name__)

from messages.sms import SMS

sms = SMS()

@app.route("/")
def main():
    return "what's up nigga"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    message = f"Replying to your message bitch, with request = {request}, form = {request.form}, keys = {request.form.keys()}, values = {request.form.values()}"

    return sms.reply_sms(message)

if __name__ == "__main__":
    app.run(debug=True)
#test
