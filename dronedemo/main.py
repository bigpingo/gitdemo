from flask import Flask
app = Flask(__name__)
print("hello my Friend~~~~~~")

@app.route("/")
def hello():
    return "Hello World~~~!"
