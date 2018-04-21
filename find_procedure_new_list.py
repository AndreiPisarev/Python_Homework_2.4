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

"""
1. Получить тек. дерикторуию, склеить с 'Migrations', получить список файлов из этой директории.
2. Отфильтровать файлы списка на sql файлы, получить список фалов для дальнейшего поиска.
3. цикл while: вводим значение для поиска, перебираем файлы, открываем, фильтруем, формируем новый список, сл. шаг while
с новым списком для поиска.
4. Выводис кол-во фалов в списке, если меньше 2-х выводим путь.
"""

import os


def list_file():

    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = os.path.join(current_dir, migrations)  # Разбил на 2 строки для получения абс. пути до файлов
    list_dir = os.listdir(dir_name)
    list_file_sql = list()
    list_file_sql = [file for file in list_dir if file.endswith('.sql')]  # Фильтруем список фалов содер. в имени '.sql'
    print("Количество .sql файлов для поиска: {}".format(len(list_file_sql)))
    return list_file_sql, dir_name  # Возвращаем список фалов sql и абс. путь до Migration


def search_in_file():

    list_file_sql, dir_name = list_file()  # Вызываем функцию list_file()

    while True:
        search = input('Введите ключевое слово (символ) для поиска:')
        new_list = []  # Каждый раз на шаге создаем пустой список для его наполнения нашими "совпадениями" по поиску

        for name_file in list_file_sql:  # Перебираем список фалов, открываем, "поиск"

            with open(os.path.join(dir_name, name_file)) as f:
                file_data = f.read()

                if search in file_data:  # Если введеное слово есть в файле, то добавляем имя фала в новый_список
                    new_list.append(name_file)
                # new_list = [name_file for name_file in list_file_sql if search in file_data]  # Даже так пробывал)

        list_file_sql = new_list  # Вот не сразу сообразил как переопределить список для нового поиска

        if len(new_list) > 2:
            print("Результат поиска:{} файлов".format(len(new_list)))
        else:
            print("Результат поиска:{} файл(а)".format(len(new_list)))
            for i in new_list:
                print("Файл(ы) находится по пути:\n{}".format(os.path.join(dir_name, i)))


if __name__ == '__main__':
    search_in_file()
