from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from services.GetRatingOfWord.common_interface import CommonInterface
import pprint


App = Flask(__name__)

App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main_database.db"

db = SQLAlchemy(App)


class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng_word = db.Column(db.String(200), nullable=False)
    rus_word = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Dictionary %r>" % self.id


with App.app_context():
    dicty = Dictionary(eng_word="dfg", rus_word="rht")
    db.session.add(dicty)
    db.session.commit()


@App.route("/", methods=["GET", "POST"])
def analyzer():
    if request.method == "POST":
        try:
            text = request.form["main_field"]
            object_handler = CommonInterface(text)
            result = object_handler.get_result()
            return render_template("response.html", articles=result)
        except:
            pass
    else:
        return render_template("query.html")


@App.route("/dictionary")
def dictionary():
    data = Dictionary.query.all()
    for x in data:
        print(x.eng_word, x.rus_word, sep="  ---  ")
    return render_template("dictionary.html")


@App.route("/workout")
def workout():
    return render_template("workout.html")


@App.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    App.run(debug=True)
