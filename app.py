from flask import flash, Flask, redirect, render_template, url_for
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "6586f3bcb8ccc14e2e3fde919f2f2031"

posts = [
    {"author": "Corey Jones", "title": "Blog Post 1", "content": "First post content", "date_posted": "April 20, 2018"},
    {"author": "Jane Doe", "title": "Blog Post 2", "content": "Second post content", "date_posted": "April 21, 2018"},
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", category="success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check your username and password", category="danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
