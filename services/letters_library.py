import string

rus_lower = "абвгдеёжзийклмнопрстуфхцчшщьъыэюя"

rus_upper = rus_lower.upper()

list_for_eng_letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

list_for_rus_letters = list(rus_lower) + list(rus_upper)

list_for_rus_letters.append(" ")

list_all_letters_base = list_for_eng_letters + list_for_rus_letters
