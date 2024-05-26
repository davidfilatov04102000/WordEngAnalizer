from .to_help import WordRepeat, WordRepeatBool
from .letters_library import list_all_letters_base
from typing import List
import nltk


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


class CheckingExisting:
    def __init__(self, *args):
        self.list_of_word = args[0]
        self.existing_word = []

    def get_result(self) -> List:
        english_vocab = set(w.lower() for w in nltk.corpus.words.words())
        for word in self.list_of_word:
            if len(word) < 2:
                continue
            elif word in english_vocab:
                self.existing_word.append(word)
        return self.existing_word


class HandlerValueAndDigitRepeat:

    """Данный класс в качестве аргумента своему инициализатору принимает список:
       2. список слов с повторениями

       Метод get_result для каждого слова в списке без повторов находит число его повторений
       в изначальном тексте. Слово и число помещает в кортеж и возвращает список таких кортежей"""

    def __init__(self, *args):
        self.list_without_repeat = list(set(args[0]))
        self.list_with_repeat = args[0]

    def get_result(self):
        list_of_items = []

        for words in self.list_without_repeat:
            if words == "":
                continue
            number = self.list_with_repeat.count(words)
            list_of_items.append(WordRepeat(words, number))
        return list_of_items


class FinderMostBigRepeat:

    """Данный класс в качестве аргумента своему инициализатору принимает список кортежей в каждом из которых
       находится слово и число его повторений в изначальном тексте. Метод get_result Находит и возвращает
       самое большое число повторений из существующих в этом списке"""

    def __init__(self, *args):
        self.list_word_repeat = args[0]

    def get_result(self):
        count = 0
        for x in self.list_word_repeat:
            if x.repeat > count:
                count = x.repeat
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
                if y.repeat == x:
                    finally_list.append(y)

        return finally_list


class CheckAvailability:

    """"""

    def __init__(self, *args):
        self.object_of_model = args[0]
        self.list_of_word_repeat = args[1]

        self.word_list_from_database = []
        self.list_of_word_repeat_bool = []

    def parsing_object(self):
        for x in self.object_of_model:
            gated_eng_word = x.eng_word
            self.word_list_from_database.append(gated_eng_word)

    def execute_checking(self):
        for obj in self.list_of_word_repeat:
            bool_value = None
            if obj.word in self.word_list_from_database:
                bool_value = 1
            else:
                bool_value = 0
            self.list_of_word_repeat_bool.append(WordRepeatBool(word=obj.word,
                                                                repeat=obj.repeat,
                                                                bool_value=bool_value))

    def get_result(self):
        return self.list_of_word_repeat_bool
