from yandexfreetranslate import YandexFreeTranslate

# yt = YandexFreeTranslate(api="web")
# yt = YandexFreeTranslate(api = "ios")
# yt.set_proxy("socks5", "localhost", 9050, "username", "password")
# print(yt.translate("en", "ru", "word"))


def lang_interpreter(word):
    yndextranslate = YandexFreeTranslate(api="ios")
    translate_word = yndextranslate.translate("en", "ru", word)
    return translate_word



