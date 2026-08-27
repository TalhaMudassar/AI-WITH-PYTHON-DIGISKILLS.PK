from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return " welcome to the flask app ! "

@app.route("/about")
def about():
    return "This is the simple route page to about section. "

@app.route("/contact")
def contact():
    return " <h2> Contact Us </h2> <p> Email: talhamudassar200@gmail.com </p> "

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)