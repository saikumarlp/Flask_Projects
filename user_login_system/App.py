from flask import Flask, render_template, request, Response
from flask import redirect, url_for
from datetime import datetime

now = datetime.now()
greet = ""
if 0 <= now.hour <= 11:
    greet = "Good Morning"

elif 12 <= now.hour <= 5:
    greet = "Good AfterNoon"

else:
    greet = "Good Evening"

app = Flask(__name__)

@app.route("/")
def entry():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submitlogin", methods = ["POST"])
def submitlogin():
    email = request.form.get("email")
    password = request.form.get("password")

    with open("userData.txt", "r") as file:
        for line in file:
            user_data = line.strip().split(" ")
            if user_data[2] == email and user_data[1] == password:
                return render_template("home.html", user = user_data[0], greet = greet)

    return render_template("login.html", error = "user not found")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/submitsignup", methods = ["POST"])
def submitsignup():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    if username == "":
        return render_template("signup.html", error = "User name required")
    
    elif password == "" or len(password) < 3:
        return render_template("signup.html", error = "Password Required")
        
    elif email == "":
        return render_template("signup.html", error = "Email Required")
    
    else:
        with open("userData.txt", "a", encoding="utf-8") as file:
            file.write(f"{username} {password} {email}\n")
    
    return render_template("home.html", user = username, greet = greet)



if __name__ == "__main__":
    app.run(debug=True)