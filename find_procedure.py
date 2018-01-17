# -*- coding: utf-8 -*-
# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_sql_files_from_dir(directory):
    # sql_files = [file for file in os.listdir(directory) if
    #              os.path.isfile(os.path.join(directory, file)) and file.endswith('.sql')]
    sql_files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and file.endswith('.sql'):
            sql_files.append(file)

    return sql_files


def search_files_by_input(files, path):
    searched_string = input('Введите строку: ')
    found_files = []
    for file in files:
        with open(os.path.join(path, file)) as f:
            if searched_string in f.read():
                found_files.append(file)

    print_and_count(found_files)

    search_files_by_input(found_files, path)


def print_and_count(lst):
    print('\n'.join(lst))
    print('Всего:', len(lst))


def main():
    migrations_path = os.path.join(current_dir, migrations)
    sql_files = get_sql_files_from_dir(migrations_path)
    search_files_by_input(sql_files, migrations_path)


# Зачем тут это условие? Какую пользу оно несёт?
if __name__ == '__main__':
    main()
