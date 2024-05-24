from .independent_classes import WordListFromString, HandlerValueAndDigitRepeat, FinderMostBigRepeat, HandlerRatingOfRepeat


class CommonInterface:

    """Данный класс объединяет работу таких классов как WordListFromString, HandlerValueAndDigitRepeat,
       FinderMostBigRepeat, HandlerRatingOfRepeat, что бы упростить получение готового результата.

       В качестве аргумента своему инициализатору он получает строку и уже при помощи метода get_result
       возвращает готовый результат в виде отсортированного списка кортежей"""

    def __init__(self, text: str):
        self.text = text

    def _query(self, class_name, *args):
        instruction = class_name
        any_object = instruction(*args)
        any_result = any_object.get_result()
        return any_result

    def get_result(self):
        only_word_list = self._query(WordListFromString, self.text)
        list_without_repeat = list(set(only_word_list))
        list_of_tuples_with_items = self._query(HandlerValueAndDigitRepeat, list_without_repeat, only_word_list)
        most_big_digit_of_repeat = self._query(FinderMostBigRepeat, list_of_tuples_with_items)
        finally_result = self._query(HandlerRatingOfRepeat, most_big_digit_of_repeat, list_of_tuples_with_items)
        return finally_result