from flask import Flask, render_template, url_for, request


App = Flask(__name__)


@App.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        text = request.form["main_field"]

        return render_template("query.html")
    else:
        return render_template("query.html")


if __name__ == "__main__":
    App.run(debug=True)
