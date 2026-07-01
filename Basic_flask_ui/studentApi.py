from flask import Flask

app = Flask(__name__)

students = {
    1 : "sai",
    2 : "Rahul",
    3 : "Ankit"
}

@app.route("/student/<int:id>")
def student(id):
    return students.get(id, "Not Found")

app.run(debug = True)
