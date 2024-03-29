from flask import Blueprint, render_template, request
from application.models import Post

main = Blueprint('main', __name__)


# view route that renders the home page
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc
                                ()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)

# view route that renders the about page
@main.route("/about")
def about():
    return render_template("about.html", title="About page")