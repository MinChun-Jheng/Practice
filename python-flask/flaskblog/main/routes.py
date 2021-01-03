from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

"""
render_template(source, **context)
**context let html can use the variables
 dummy post data
posts = [
    {
        'author': 'MinChun',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Dec 21, 2020'
    },
    {
        'author': 'Jheng',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Dec 21, 2020'
    }
]
"""

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
