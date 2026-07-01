# /search?name=Sai

from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Searching for {name}"
# http://127.0.0.1:5000/search?name=sai


@app.route("/searching")
def searching():
    name = request.args.get("name")
    age = request.args.get("age")

    print(request.args)

    return f"{name} is {age} years old."
# http://127.0.0.1:5000/searching?name=sai&age=20

app.run(debug = True)
