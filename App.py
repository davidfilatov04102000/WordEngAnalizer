from flask import Flask, render_template, url_for


App = Flask(__name__)


@App.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("query.html")


if __name__ == "__main__":
    App.run(debug=True)
