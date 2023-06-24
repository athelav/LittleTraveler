from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Tim")


@views.route("/profile")
def profile():
    # args = request.args
    # name = args.get('name')
    return render_template("profile.html")


@views.route("/welcome")
def welcome():
    return render_template("welcome.html")


@views.route("/title")
def title():
    return render_template("title.html")


@views.route("/homepage")
def homepage():
    return render_template("homepage.html")


@views.route("/plane")
def plane():
    return render_template("plane.html")


@views.route("/train")
def train():
    return render_template("train.html")


@views.route("/passport")
def passport():
    return render_template("passport.html")


@views.route("/resources")
def resources():
    return render_template("resource.html")


@views.route("/more")
def more():
    return render_template("more.html")


@views.route("/moreTitle")
def moreTitle():
    return render_template("moreTitle.html")


@views.route("/moreWelcome")
def moreWelcome():
    return render_template("moreWelcome.html")


@views.route("/json")
def get_json():
    return jsonify({'name': 'time', 'coolness': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))


@views.route("/test")
def test():
    return render_template("test.html")
