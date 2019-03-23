from flask import Flask, request
app = Flask(__name__)

<<<<<<< HEAD
=======
from messages.sms import SMS

sms = SMS()
>>>>>>> 9f163130f4c7dc6e689ba5a58d7b8c4273f25c25

@app.route("/")
def main():
    return "what's up nigga"

<<<<<<< HEAD

@app.route("/sms")
def hello():
    return "Hello World!"
=======
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    message = f"Replying to your message bitch, with request = {request}, form = {request.form}, keys = {request.form.keys()}, values = {request.form.values()}"

    return sms.reply_sms(message)
>>>>>>> 9f163130f4c7dc6e689ba5a58d7b8c4273f25c25


if __name__ == "__main__":
    app.run(debug=True)
