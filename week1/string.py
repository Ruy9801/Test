# строки - неизменяемый тим данных  который предназначен для хранения текста
# заключаются в одинарные и двойные ковычки

# string1 = 'строка с одиранрыми ковычками'
# string2 = "стора с двойными кавычками"
# error = "Dont't do it'
# string3 = "Don't"
# string4 = "Makers"

# print(string4)

# string = ''''''
# текст '""'""'"'"
# ''' тут можно ставить любые ковычки

# print('Hello\nworld') - перенос на следующую строку
# print('Hello\n\tworld') - перенос по табуляции

# while True:
    # string = '1'



# =========Конкатенация (сложение)============

# S1 = 'spam'
# S2 = 'eggs'

# print(S1 + S2)

# # ============Дублирование строки===============

# print('spam' * 3)

# # ===============Длина строки (функция len)=================

# len('spam')

# # ================Доступ по индексу==================

# S = 'spasm'

# print(S[0])

# # =================Извлечение среза===================

# s = 'spameggs'

# print(s[3])

# print(s[2:-2])

# print(s[::-1])

# print(s[3:5:-1])

# print(s[2::2])



# # ======================Форматирование строк=======================

# # format() - возвращает отформатированную версию строки, заменяя идентификаторы в фигурных скобках. Идентификаторы могут быть позиционными, числовыми индексами, ключами словарей, именами переменных.

# name = 'Steve'
# hello = 'Hello, {}'.format(name)

# print(hello)

# # f'string - внутри f'строки в паре фигурных скобок укказываются имена переменных, которые надо подставить:

# namee = 'John'
# surname = 'Snow'

# print(f"{namee},{surname}")

# # % - Структура данных типа форматирования выглядит так:

# print('Hellj, %s!' % 'Vasya')


# Методы типов данных - функции, к которым мы обращаемся через точку



# Методы на is 

# все что начинается на is  возвращает True/False 

# string = 'hello world'

# isdigit() - возвращает True если строка полностью состоит из цифр

# print(string.isdigit())


# isalpha() - возвращает True если строка полностью состоит из букв

# print(string.isapha())


# isalnum() - состоит ли строка из цифр или букв

# string = 'Ryu8998'
# print(string.isalnum())  # --- False


# islower() - состоит ли строка из символов в нижнем регистре

# print(string.islower())


# isupper() - состоит ли строка из символов в верхнем регистре

# isspase() - состоит ли строка из неотображаемых символов

# istitle() - начинаются ли слова в строке с заглавной буквы

# print(string.istitle())


# print(dir(str)) посмотреть все методы типа данных


# lower() - переводит целую строку в нижний регистр

# print('HELLO'.lower())


# upper() - переводит целую строку в верхний регистр

# print('sdkjlj'.upper())


# swapcase() - переводит символы в противоположный регистр

# print('Hello World'.swapcase())


# title() - переводит каждую букву слова в строке в верхний регистр

# print('hello world'.title())


# strip() - убирает пробелы в начале и в конце строки

# print('    Hellow     '.strip())


# lstrip() rstrip() - убирает слева или справа


# replace() - меняет местами или заменяет

# print('hsaap'.replace('hsaap', 'sheep' 1))


# split() - делит стоку по разделителю и возвращает массив list() 

# print('You Are'.split())


# индекс - порядковый номер символа в строке

# 'hello world'

# # h e l l o  w o r l d
# # 0 1 2 3 4 5 6 7 8 9 10



# : - подстрока строки СРЕЗЫ
# string[start:end:step]


# string = 'hello world'
# print(string[0:5])
# print(string[0:6])
# print(string[:])
# print(string[0:5][2:4][:1])
# print(string[6:])
# print(string[:11:2])
# print(string[::3])
# print(string[::-1])


# capitalize() - переводит первый символ в верхний регистр

# print('hello'.capitalize())


# endswith(element) возвращает True если строка заканчивается на element

# print('hello world'.endswith('!'))


# startswith(element) - возвращает True если строка начется на element

# print('makers'.startswith('k',2))


# count(element) - считает количество вхождений element в строке

# print('makers'.count())


# len() - считает длину строк

# print(len(dude))


# index()

# print('hello'.index('l'))

# indexs = 'hello'.index('o')
# print(indexs)

# find()

# print('lello'.find('l'))


# id()

# a = 'hello'
# print(id(a))


# join() - применяет в себя список

# text = "Milk, Bread, Water"

# text = "Snow"
# split = list(text)
# print(split)

# joined = "*".join(split)
# print(joined)

# text = 'coder'

# print(text[-1] + text[1:4])

# address = '1.1.1.1'

# print(address.replace('.', '[.]'))

# Вывод фамилию с инициалами;

# name = input('Введите свое имя:')

# you = name.split()

# your_in = you[0].capitalize() + ' ' +you[1][0].capitalize() +' ' + you[2][0].capitalize()

# print(your_in)


# ========Проверка слов в if============

# res = input('Ввидите слово:')

# # if res.find('сок') != -1: <> выводит индекс

# if 'сок' in res:
#     print(True)
# else:
#     print(False)



# res = input('Введите имя, фамилия и возраст через пробел:')

# res0 = res.split()

# res2 = res0[0].replace('a','')
# res1 = list(res0[1])
# res11 = "*".join(res1)
# print(res1)

# res3 = 'Вывод:' + (res2 + res1) * res[2]

# print(res3)

# res3 = res2 + res1[2] * res2

# print('Результат:' + res3)

# print(ress)



# Задание 11
# В переменную num из вкладки INPUT попадает число, которое обозначает код символа по таблице ASCII(https://ru.wikipedia.org/wiki/ASCII)
# Определить, является ли введенное число кодом английской буквы.


# num = int(input()) 
# if (num >= 65 and num <= 90) or (num >= 97 and num <= 122): 
#     print(f"Это буква \"{chr(num)}\"") 
# else: 
#     print(f"Это не буква, а символ \"{chr(num)}\"")
