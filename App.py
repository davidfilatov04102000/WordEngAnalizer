from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from services.GetRatingOfWord.common_interface import CommonInterface
from services.GetRatingOfWord.to_help import query
from services.LanguageInterpreter import lang_interpreter
from services.checkavailability_abs import abstract_check_availability
from services.for_workout import checking
import pprint
import random

for_temporary_storage = None
list_for_temporary_storage = None
the_set_value = None
list_for_temporary_message = []

App = Flask(__name__)

App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main_database.db"

db = SQLAlchemy(App)


class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng_word = db.Column(db.String(200), nullable=False)
    rus_word = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Dictionary %r>" % self.id


# with App.app_context():
#     db.create_all()


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


@App.route("/dictionary", methods=["GET", "POST"])
def dictionary():
    data = Dictionary.query.all()
    button_name = 1

    datas = {
        "table": data,
        "button": button_name
    }

    if request.method == "POST":
        req_obj = request.form
        button_name = int(str(req_obj.keys())[12:-3])

        datas = {
            "table": data,
            "button": button_name
        }
        return render_template("dictionary.html", articles=datas)
    else:
        return render_template("dictionary.html", articles=datas)


@App.route("/workout", methods=["GET", "POST"])
def workout():
    global the_set_value
    global list_for_temporary_storage
    global list_for_temporary_message

    mode = 1

    if request.method == "POST":
        user_answer = request.form["user_answer"]
        print(user_answer)
        bot_answer = checking(the_set_value, user_answer)
        print(bot_answer)

        list_for_temporary_message.append(user_answer)
        list_for_temporary_message.append(bot_answer)
        print(list_for_temporary_message)

        dataset = {
            "messages": list_for_temporary_message
        }

        return render_template("workout.html", articles=dataset)
    else:
        data = Dictionary.query.all()
        list_for_temporary_message.clear()
        the_set_value = None

        list_for_temporary_storage = data.copy()
        the_set_value = random.choice(data)

        if mode == 1:
            list_for_temporary_message.append(the_set_value.eng_word)
        else:
            list_for_temporary_message.append(the_set_value.rus_word)

        datas = {
            "bot_question": the_set_value,
            "mode": mode
        }

        return render_template("workout.html", articles=datas)


@App.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    App.run(debug=True)
