# цикл for позволяет пройтись по каждому элементу итерируемого объекта

# name = 'John'

# for letter in name:
#     print(letter)


# '''
# Синтаксис:

# name = 'john'

# for <var_name> in name:
#     pass

# '''

# # ================= Условные операторы

# money = 100

# if money > 100:
#     print('Покупаю 2л колу')  
# elif money == 0:
#     print('I will have to still')
# else:
#     print('Покупаю кефир')

# '''
# Синтакис:

# if < Условие1 >:
#     pass
# elif < Условие2 >:
#     pass
# else:
#     pass
# '''

# x = 87
# y = 23

# resolt = x / y

# if x / y:
#     print(f'Частное: {resolt}')

# Задание 8
# В переменные x, y попадают числа вводимые пользователем. Проверить делится ли первое число на второе без остатка.

# x = int(input()) 
# y = int(input()) 
# if x % y == 0: 
#     print('x делится на y') 
#     d = x//y 
#     print(f'Частное: {d}') 
# else: 
#     print('x не делится на y') 
#     a = x // y 
#     print(f'Частное: {a}') 
#     b = x % y 
#     print(f'Остаток: {b}')


# Задание 9
# В переменную year попадает число-год от пользователя.
# Определите, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.

# year = int(input())

# if year%4 == 0 and year%100 != 0 : 
#     print('YES') 
# elif year%400 == 0: 
#     print('YES') 
# else: 
#     print('NO')

# string = '123214'
# print(string[3:6])
# print(string[0:3])

# Логические выражения и операторы


#  boolen

# pritn(bool(0))
# bool(3)
# bool(-233)
# bool('hello')
# bool(' ')
# bool('') False

# a = 3
# == --> bool
# print(int('2' == 2))

# != - не равно

# print( 5 != 5) - False 
# print( 2 != 3) - True 

# > < -- bool 


# Логические операторы

# and - голическое и
# or - логическое или
# not - логическое отрицание

# a = 5
# b = 6

# print(a == 5 and b == 6) - True 
# a == 3 and b == 3 - False 

# print(a == 5 or b == 7)

# print(not True)
# print(not False)
# not a == 5 - False 
# not a == 4 - True 

# Оператор индетификации

# in - > проверяет наличие элемента

# сравнивание

# == - сравнение по значению 
# is - сравнение по ячейкам памяти


# str_ = 'hello'

# if 'e' in str_:
#     print('worked')


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(id(a))
# print(id(b))
# print(a is b) - False
# print(a == b) - True

# bool('None')
# bool(None)

# a = None 
# print(a is None)



# Условные операторы - нужны для того, чтобы при разных входных данных код работал по разному


# if a:
#     print('worked')

# age = int(input('Введите ваш возраст:'))

# if age >=18:
#     print('Доступ разрещен!')
# elif age <= 17:
#     print('в Доступе отказана')


# number = int(input('Ввидите число:'))

# if number % 2 == 0:
#     print('ch')
# else:
#     print('no')

# import random

# num = int(input('Ввидите число от 1 до 5: '))

# numm = random.randint(1, 5)

# if num == numm:
#     print('Вы угадали число')
# else:
#     print('Вы не угадали число')


# handu = input('Ваш выбор: ')

# handb = random.randint('Камень', 'Ножницы', 'Бумага')

# if 'Камень' in handu and 'Ножницы' in handb:
#     print('Ваш выбор: Камень')
#     print('Выбор компьтера: Ножницы')
#     print('Вы выиграли!')
# elif 'Ножницы' in handu and 'Бумага' in handb:
#     print('Ваш выбор: Ножницы')
#     print('Выбор компьтера: Бумага')
#     print('Вы выиграли!')
# elif 'Бумага' in handu and 'Камень' in handb:
#     print('Ваш выбор: Бумага')
#     print('Выбор компьтера: Камень')
#     print('Вы выиграли!')
# elif 'Камень' in handu and 'Камень' in handb:
#     print('Ваш выбор: Камень')
#     print('Выбор компьтера: Камень')
#     print('У вас Ничья!')
# elif 'Ножницы' in handu and 'Ножницы' in handb:
#     print('Ваш выбор: Ножницы')
#     print('Выбор компьтера: Ножницы')
#     print('У вас Ничья!')
# elif 'Бумага' in handu and 'Бумага' in handb:
#     print('Ваш выбор: Бумага')
#     print('Выбор компьтера: Бумага')
#     print('У вас Ничья!')
# elif 'Камень' in handu and 'Бумага' in handb:
#     print('Ваш выбор: Камень')
#     print('Выбор компьтера: Бумага')
#     print('Вы Проиграли!')
# elif 'Бумага' in handu and 'Ножницы' in handb:
#     print('Ваш выбор: Бумага')
#     print('Выбор компьтера: Ножницы')
#     print('Вы Проиграли!')
# elif 'Ножницы' in handu and 'Камень' in handb:
#     print('Ваш выбор: Ножницы')
#     print('Выбор компьтера: Камень')
#     print('Вы Проиграли!')
# тернарные операторы это условие в одну строку

# тела1 if условие else тело2
# a = 5
# res = 'Hello' if a == 4 else 'Bye'

# маржовые операторы позволяет нам как присваивать значение переменной, так и  возвращает ее значение

# print(num = 15)
# print(num := 15)
# print(num)

# operator = input('Введите необходимый оператор:(+, -, *, /,)')
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))

# if operator == '+':
#     print(number1 + number2)



# FizzBuzz

# num = input('Введите имя: ')
# num1 = int(input('Сколько у вас друзей? '))


# name = 'друзей'
# name1 = 'друг'

# if num1 > 1 or num1 == 0:
#     print(f'У {num} {num1} {name}!')
# elif num1 <= 1:
#     print(f'У {num} {num1} {name1}')


# if num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0 and num % 3 == 0:
#     print('FizzBuzz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print(num)

# num = int(input('Введите число1: '))
# num1 = int(input('Введите число2: '))
# num2 = int(input('Введите число3: '))

# if num==num1==num2==num:
#     print('Равносторонний треугольник!')
# elif num==num1!=num2:
#     print('Равнобедренный треугольник!')
# elif num!
# num*num1 == 90 or num*num2 ==90 or num1*num2==90:


# password = input('Введите парель: ')

# if  password.isdigit() and len(password) >= 8:
#     print('Ваш пароль сохранен!')
# elif password.isalpha() :
#     print('Ваш пароль должен хранить только числа!')

# if len(password) <= 7:
#     print('Ваш пароль должен содержать не менее 8 символов')

# bal = input("Введите свои баллы по математике, английскому языку и литературе через запятую: ")

# ball = bal.replace(',','')

# ball1 = ball.split()

# resb = int((ball1[0] + ball1[1] + ball1[2]) / 2)

# if resb >= 70:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {resb}')
# elif resb <=69:
#     print(f'У вас недопуск с экзаменам. Ваш средний балл составляет {resb}')

# string = 'RyuDzaky'

# print(string[-1])
# print(string[-2:])
# print(string[::-1])
# print(len(string))

# string = 'The quick brown fox jumps over the lazy dog'

# print(string.replace('o','*'))

# usser = input("Введите имя, фамилию, возраст и город, в котором вы проживаете: ")
# name =  usser.split()
# namef = name[0]
# names = name[1]
# age = name[2]
# city = name[3]
# print(f'Вас зовут {namef} {names}, Ваш возраст: {age}, Вы проживаете в городе {city}')


# number = int(input('Введите число: '))

# if number > 5:
#     print('True')
# elif number < 5:
#     print('False')

