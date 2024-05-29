from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from services.GetRatingOfWord.common_interface import CommonInterface
from services.GetRatingOfWord.to_help import query
from services.LanguageInterpreter import lang_interpreter
from services.checkavailability_abs import abstract_check_availability
from services.for_workout import checking
import random

for_temporary_storage = None
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


@App.route("/", methods=["GET", "POST"])
def analyzer():
    global for_temporary_storage

    dicty = list(db.session.execute(db.select(Dictionary).order_by(Dictionary.eng_word)).scalars())

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

                dicty_2 = list(db.session.execute(db.select(Dictionary).order_by(Dictionary.eng_word)).scalars())

                result_check = abstract_check_availability(dicty_2, for_temporary_storage)

                for_temporary_storage = result_check
                return render_template("response.html", articles=result_check)

            except:
                return "произошла ошибка при сохранении данных"

    else:
        return render_template("query.html")


@App.route("/dictionary", methods=["GET", "POST"])
def dictionary():
    data = list(db.session.execute(db.select(Dictionary).order_by(Dictionary.eng_word)).scalars())

    button_number = 1

    datas = {
        "table": data,
        "button": button_number
    }

    if request.method == "POST":
        req_obj = request.form
        button_number = int(str(req_obj.keys())[12:-3])

        datas = {
            "table": data,
            "button": button_number
        }

        return render_template("dictionary.html", articles=datas)

    else:
        return render_template("dictionary.html", articles=datas)


@App.route("/edit_dictionary", methods=["GET", "POST"])
def edit_dictionary():
    data = list(db.session.execute(db.select(Dictionary).order_by(Dictionary.eng_word)).scalars())

    if request.method == "POST":
        id_of_object = int(request.form["button_save_word"])
        datas = db.get_or_404(Dictionary, id_of_object)

        datas.eng_word = request.form["word"]
        datas.rus_word = request.form["repeat"]

        try:
            db.session.commit()

            return render_template("edit.html", articles=data)

        except:
            return "Произошла ошибка"

    else:
        return render_template("edit.html", articles=data)


@App.route("/delete_word/<int:id>")
def delete_word(id):
    data = db.get_or_404(Dictionary, id)

    try:
        db.session.delete(data)
        db.session.commit()

        return redirect("/edit_dictionary")

    except:
        return "Произошла ошибка"


@App.route("/workout", methods=["GET", "POST"])
def workout():
    global the_set_value
    global list_for_temporary_message

    mode = 1

    if request.method == "POST":
        user_answer = request.form["user_answer"]

        bot_answer = checking(the_set_value, user_answer)

        list_for_temporary_message.append(user_answer)
        list_for_temporary_message.append(bot_answer)

        dataset = {
            "messages": list_for_temporary_message
        }

        return render_template("workout.html", articles=dataset)
    else:
        data = list(db.session.execute(db.select(Dictionary).order_by(Dictionary.eng_word)).scalars())

        list_for_temporary_message.clear()
        the_set_value = None

        try:
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
        except:
            return render_template("error.html")


@App.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    App.run(debug=True)
