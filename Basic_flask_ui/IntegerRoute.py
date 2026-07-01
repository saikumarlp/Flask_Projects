from flask import Flask

app = Flask(__name__)

@app.route("/square/<int:num>")
def square(num):
    return f"Square of number {num} is {str(num * num)}"

app.run(debug = True)