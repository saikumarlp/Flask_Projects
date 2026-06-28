from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))

        else:
            return Response("Invalid credentails. Try Again", mimetype="text/plain") 
        # mimetype = default (text/html)
    
    return """
        <h2>Login Page </h2>
        <form method = "post" >
            username : <input type = "text" name = "username"> <br>
            password : <input type = "password" name = "password"> <br>
            <input type = "submit" value = "login">
        </form>
"""

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome, {session["user"]}! </h2>
        <a href={url_for('logout')}>Logout</a>
    """
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("user", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)