from flask import Flask, request

app = Flask(__name__)


# route decorator
@app.route("/")
def indexPage():
    return "Hello World!" 

# get - ask server to serve the data
# post - sending data to server

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "GET":
        return "You are only viewing the form"
    else:
        return "You sent Data!!"

