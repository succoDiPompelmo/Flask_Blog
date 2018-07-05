from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '888'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # DEFINE HOW OUR OBJECT IS PRINTED OUT
    def __repr__(self):
        return self.email


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # DEFINE HOW OUR OBJECT IS PRINTED OUT
    def __repr__(self):
        return self.title

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

# REGISTRATION ROUTE
@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash('Account created','success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register",form=form)

# LOGIN ROUTE
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash("You have been logged in !", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful', 'danger')
    return render_template("login.html", title="Login",form=form)

if __name__ == "__main__":
    app.run(debug=True)