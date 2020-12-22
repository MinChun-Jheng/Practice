from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# render_template will look up  html file in templates folder
# url_for find the exact location of routes
app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'

posts = [
    {
        'author': 'MinChun',
        'title': 'Post Test 1',
        'content': 'First post content',
        'date_posted': 'Dec 21, 2020'
    },
    {
        'author': 'Jheng',
        'title': 'Post Test 2',
        'content': 'Second post content',
        'date_posted': 'Dec 21, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) #


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # f is .format above python 3.6
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfu. Please check')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
