from .letters_library import list_for_eng_letters


def query(class_name, *args):
    instruction = class_name
    any_object = instruction(*args)
    any_result = any_object.get_result()
    return any_result


def eng_isalpha(word: str):
    i = 0
    for e in word:
        if e in list_for_eng_letters:
            i += 1
    return i == len(word)


class WordRepeat:
    def __init__(self, word: str, repeat: int):
        self.word = word
        self.repeat = repeat


class WordRepeatBool(WordRepeat):
    def __init__(self, word: str, repeat: int, bool_value: int):
        super().__init__(word=word, repeat=repeat)
        self.bool_value = bool_value
