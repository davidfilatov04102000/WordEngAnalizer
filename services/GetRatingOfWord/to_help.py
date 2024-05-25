def query(class_name, *args):
    instruction = class_name
    any_object = instruction(*args)
    any_result = any_object.get_result()
    return any_result


class WordRepeat:
    def __init__(self, word: str, repeat: int):
        self.word = word
        self.repeat = repeat


class WordRepeatBool(WordRepeat):
    def __init__(self, word: str, repeat: int, bool_value: int):
        super().__init__(word=word, repeat=repeat)
        self.bool_value = bool_value
