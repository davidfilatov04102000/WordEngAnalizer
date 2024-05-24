from flask import Flask, render_template, url_for, request
from services.common_interface import CommonInterface
import pprint


App = Flask(__name__)


@App.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        text = request.form["main_field"]
        object_handler = CommonInterface(text)
        result = object_handler.get_result()
        pprint.pprint(result)
        return render_template("query.html")
    else:
        return render_template("query.html")


if __name__ == "__main__":
    App.run(debug=True)
