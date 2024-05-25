from .independent_classes import WordListFromString, HandlerValueAndDigitRepeat, FinderMostBigRepeat
from .independent_classes import HandlerRatingOfRepeat, CheckAvailability
from .to_help import query


class CommonInterface:

    """Данный класс объединяет работу таких классов как WordListFromString, HandlerValueAndDigitRepeat,
       FinderMostBigRepeat, HandlerRatingOfRepeat, CheckAvailability что бы упростить получение готового результата.

       В качестве аргумента своему инициализатору он получает строку и объект модели и уже при помощи метода get_result
       возвращает готовый результат в виде отсортированного списка кортежей"""

    def __init__(self, *args):

        self.text = args[0]
        self.object_model = args[1]

    def get_result(self):
        only_word_list = query(WordListFromString, self.text)

        list_of_tuples_with_items = query(HandlerValueAndDigitRepeat, only_word_list)

        most_big_digit_of_repeat = query(FinderMostBigRepeat, list_of_tuples_with_items)

        sorted_list_word_repeat = query(HandlerRatingOfRepeat, most_big_digit_of_repeat, list_of_tuples_with_items)

        object_finally_result = CheckAvailability(self.object_model, sorted_list_word_repeat)

        object_finally_result.parsing_object()

        object_finally_result.execute_checking()

        finally_result = object_finally_result.get_result()

        return finally_result
