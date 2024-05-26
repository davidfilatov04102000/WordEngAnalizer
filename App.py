from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from services.GetRatingOfWord.common_interface import CommonInterface
from services.GetRatingOfWord.to_help import query
from services.LanguageInterpreter import lang_interpreter
from services.checkavailability_abs import abstract_check_availability
import pprint

for_temporary_storage = None

App = Flask(__name__)
App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main_database.db"
db = SQLAlchemy(App)


class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng_word = db.Column(db.String(200), nullable=False)
    rus_word = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Dictionary %r>" % self.id


@App.route("/", methods=["GET", "POST"])
def analyzer():
    global for_temporary_storage
    dicty = Dictionary.query.all()

    if request.method == "POST":
        try:
            text = request.form["main_field"]
            result = query(CommonInterface, text, dicty)
            for_temporary_storage = result.copy()
            return render_template("response.html", articles=result)
        except:
            word = request.form["word"]
            rus_word = lang_interpreter(word)

            dict_object = Dictionary(eng_word=word, rus_word=rus_word)

            try:
                db.session.add(dict_object)
                db.session.commit()
                dicty_2 = Dictionary.query.all()
                result_check = abstract_check_availability(dicty_2, for_temporary_storage)
                for_temporary_storage = result_check
                return render_template("response.html", articles=result_check)

            except:
                return "произошла ошибка при сохранении данных"

    else:
        return render_template("query.html")


@App.route("/dictionary")
def dictionary():
    data = Dictionary.query.all()
    return render_template("dictionary.html", articles=data)


@App.route("/workout")
def workout():
    return render_template("workout.html")


@App.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    App.run(debug=True)
