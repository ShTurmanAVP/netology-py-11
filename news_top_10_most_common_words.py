import chardet

files = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']

for file in files:
    with open('news/'+file, 'rb') as f:
        data = f.read()
        words = data.decode(chardet.detect(data)['encoding']).split()

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

        print(file)
        print(''.join('{:<20}: {:<5}\n'.format('\"'+word+'\"', count) for count, word in top_words[:10]), end='\n')
