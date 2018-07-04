from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        "title": "Pino",
        "author": "Piano",
        "date_posted": "Ciao",
        "content": "Nothing"
    }
]

# HOME PAGE
@app.route("/")
def hello():
    return render_template("home.html", posts=posts)

# ABOUT PAGE
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)