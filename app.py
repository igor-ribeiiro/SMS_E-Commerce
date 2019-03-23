from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "what's up nigga"

@app.route("/sms")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
