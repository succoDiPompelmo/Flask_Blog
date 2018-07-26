from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main', __name__)


# HOME PAGE
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    print posts
    return render_template("home.html", posts=posts)

# ABOUT PAGE
@main.route("/about")
def about():
    return render_template("about.html")