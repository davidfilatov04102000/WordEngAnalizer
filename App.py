from flask import Flask, render_template, url_for, request
from services.common_interface import CommonInterface
import pprint


App = Flask(__name__)


@App.route("/", methods=["GET", "POST"])
def analyzer():
    if request.method == "POST":
        text = request.form["main_field"]
        object_handler = CommonInterface(text)
        result = object_handler.get_result()
        return render_template("response.html", articles=result)
    else:
        return render_template("query.html")


@App.route("/dictionary")
def dictionary():
    return render_template("dictionary.html")


@App.route("/workout")
def workout():
    return render_template("workout.html")


@App.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    App.run(debug=True)
