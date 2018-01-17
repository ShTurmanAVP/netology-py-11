# -*- coding: utf-8 -*-
import chardet
import json
import xml.etree.ElementTree as ETree
import re

files = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt',
         'newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json',
         'newsafr.xml', 'newscy.xml', 'newsfr.xml', 'newsit.xml']
# files = ['newsafr.txt', 'newsafr.xml']


def main():
    for file in files:
        with open('news/' + file, 'rb') as f:
            data = get_decoded_data_from_opened_file(f)

            if file.endswith('.txt'):
                words = data.split()

            elif file.endswith('.json'):
                json_data = json.loads(data)
                words = []
                for item in json_data['rss']['channel']['items']:
                    for key, value in item.items():
                        if key == 'description' or key == 'title':
                            words += value.split()

            elif file.endswith('.xml'):
                xml_data = ETree.fromstring(data)
                words = []
                for item in xml_data.iter('item'):
                    title_text = item.find('title').text
                    description_text = item.find('description').text

                    words += get_cleaned_from_tags_and_punctuation_marks(title_text).split()
                    words += get_cleaned_from_tags_and_punctuation_marks(description_text).split()

            print(file)
            print_top_n_most_common_words(words)
            # print(words)


def get_cleaned_from_tags_and_punctuation_marks(text):
    clean_text = re.sub('<.*?>|,|\.|\?|!|-|\(|\)|/|"|«|»|:|;|%', ' ', text)
    return clean_text


def get_decoded_data_from_opened_file(file):
    raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']
    # print(encoding, file)
    return raw_data.decode(encoding)


def print_top_n_most_common_words(words):
    word_occurrences = {}
    for unique_word in set(words):
        if len(unique_word) <= 6:
            continue

        counter = 0
        for word in words:
            if word == unique_word:
                counter += 1
        word_occurrences[unique_word] = counter

    top_words = sorted(((count, word) for word, count in word_occurrences.items()), reverse=True)

    print(''.join('{:<20}: {:<5}\n'.format('\"'+word+'\"', count) for count, word in top_words[:10]), end='\n')


main()
