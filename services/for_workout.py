from .GetRatingOfWord.to_help import eng_isalpha
from fuzzywuzzy import fuzz


def checking_answer(model_obj, answer):
    comparison = fuzz.ratio(model_obj, answer)
    if comparison == 100:
        return "Полностью верно"
    elif comparison > 90:
        return "Верно, но есть ошибки"
    else:
        return "Неверно"


def checking(model_object, answer: str):
    what_lang = eng_isalpha(answer)
    if what_lang is False:
        return checking_answer(model_object.rus_word, answer)
    else:
        return checking_answer(model_object.eng_word, answer)







