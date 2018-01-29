import os
import requests


# https://translate.yandex.net/api/v1/tr.json/translate?id=172f2021.5a6e4803.0daa878e-2-0&srv=tr-text&lang=ru-en&reason=auto
def translate_it(text, target_lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :param target_lang: <str> target language.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    # на самом деле нет необходимости указывать source_lang. API автоматически определяет его при отсутствии
    # lang = source_lang + '-' + target_lang
    lang = target_lang

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    # why not just return ' '.join(response['text'])?
    return ' '.join(response.get('text', []))


def translate_files(source_path, target_path, target_lang='ru'):
    for file in os.listdir(source_path):
        suffix = '.txt'
        if os.path.splitext(file)[1] == suffix:

            if not os.path.exists(target_path):
                os.mkdir(target_path)

            target_file = os.path.splitext(file)[0] + '-' + target_lang.upper() + suffix
            with open(os.path.join(source_path, file)) as sf, open(os.path.join(target_path, target_file), 'w') as tf:
                print('translating', file)
                text = sf.read()
                tf.write(translate_it(text, target_lang))


SOURCE = 'news_for_translation'
TARGET = os.path.join(SOURCE, 'translations')

translate_files(SOURCE, TARGET)
