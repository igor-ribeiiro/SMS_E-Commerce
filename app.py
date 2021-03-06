from flask import Flask, request, jsonify
from database.operations import get_items, add_user, update_address, update_name, delete_item
from messages.sms import SMS
from messages.messages_manager import MessagesManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sms = SMS()

@app.route("/", methods=["GET", "POST"])
def main():
    return "what's up nigga"


@app.route("/shelf", methods=["GET", "POST"])
def shelf():
    print("gogo")
    try:
        all_items = get_items()
        items = [item.as_dict() for item in all_items]
        items.sort(key=lambda item: item["descricao"])
        return jsonify(result=items)
    except Exception as E:
        print(E)
        return jsonify(result=[])


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    from_number = request.form['From']
    sent_message = request.form['Body']
    print("")
    print("Received a message")
    print(f"sent_message = {sent_message} and from_number = {from_number}")

    messages_manager = MessagesManager(from_number, sent_message)
    reply_message = messages_manager.get_message_to_be_sent()

    # reply_message += f", with fromNumber = {from_number}"
    print(f"Reply message = {reply_message}")
    return sms.reply_sms(reply_message)

if __name__ == "__main__":
    app.run(debug=True)
