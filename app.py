from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# creating an app instance

# use a decorator @ to define the route to our webpage
@app.route("/")
# setting up a default page
def index():
    return "Welcome to DevOps team"


@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            print((type(request.form["username"]), request.form["password"]))
            error = "Invalid Credentials. Please try again."
        else:
            return redirect(url_for("home"))
    return render_template("login.html", error=error)

@app.route("/welcome/")
def welcome():
    return "Welcome onboard!"

# create two more routes, add the functionality for email and password


if __name__=='__main__':
    app.run(debug=True)
