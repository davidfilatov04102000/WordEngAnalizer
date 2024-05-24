from .letters_library import list_all_letters_base
from typing import List


class WordListFromString:

    """ Данный класс в качестве аргумента инициализатору принимает строку, а метод get_result
        убирает из этой строки все что не равняется буквам или пробелу и возвращает список всех слов
        которые есть в тексте"""

    def __init__(self, *args):
        self.text = str(args[0])

    def get_result(self) -> List:
        text_list = list(self.text.lower())

        list_only_letter = []

        for letter in text_list:
            if letter in list_all_letters_base:
                list_only_letter.append(letter)

        finally_text = "".join(list_only_letter)

        return finally_text.split(" ")


class HandlerValueAndDigitRepeat:

    """Данный класс в качестве аргумента своему инициализатору принимает два списка:
       1. список слов без повторений,
       2. список слов с повторениями

       Метод get_result для каждого слова в списке без повторов находит число его повторений
       в изначальном тексте. Слово и число помещает в кортеж и возвращает список таких кортежей"""

    def __init__(self, *args):
        self.list_without_repeat = args[0]
        self.list_with_repeat = args[1]

    def get_result(self):
        list_of_items = []

        for words in self.list_without_repeat:
            if words == "":
                continue
            number = self.list_with_repeat.count(words)
            list_of_items.append((words, number))
        return list_of_items


class FinderMostBigRepeat:

    """Данный класс в качестве аргумента своему инициализатору принимает список кортежей в каждом из которых
       находится слово и число его повторений в изначальном тексте. Метод get_result Находит и возвращает
       самое большое число повторений из существующих в этом списке"""

    def __init__(self, *args):
        self.args = args

    def get_result(self):
        count = 0
        for x in self.args[0]:
            if x[1] > count:
                count = x[1]
        return count


class HandlerRatingOfRepeat:

    """Данный класс в качестве аргумента своему инициализатору принимает
       1. Максимальное число повторений
       2. Список кортежей (слово + колличество его повторов в большом тексте)

       Метод get_result создает и возвращает отсортированный список кортежей
       (слово + колличество его повторов в большом тексте) по убыванию колличества повторений в большом тексте.

       Сначала расположены кортежи с самыми большими числами повторений и далее по убыванию."""

    def __init__(self, *args):
        self.max_reply = args[0]
        self.items_list = args[1]

    def get_result(self):
        finally_list = []

        for x in range(self.max_reply, 0, -1):
            for y in self.items_list:
                if y[1] == x:
                    finally_list.append(y)

        return finally_list