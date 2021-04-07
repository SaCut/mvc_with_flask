from flask import Flask, render_template

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

@app.route("/welcome/")
def welcome():
    return "Welcome onboard!"


if __name__=='__main__':
    app.run(debug=True)
