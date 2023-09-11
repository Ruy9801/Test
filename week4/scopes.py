# Пространство имен 


# 1) builtins (встроеннное имен) - все что встроенно в оболочку питона 

# print(dir(__builtins__))


# ==========================================================================


# 2) global - все переменные внутри файла которые мы создали

# globals - возвращает словарь с глобальными переменными 

# a = 8
# b = 'hello'


# print(globals()['a'])
# print(a is globals()['a'])
# globals()['c'] = 'hello'
# globals()['c'] = 'hello world'
# print(globals()['c'])

# x = 10

# def func():
#     global x 
#     x = 20
#     print(x, 'x is local')

# func()
# print(x, 'x is global')

# global - позволяет ментять значение глобальной перменной, находясь в локальной области видимости 


# =====================================================================================


# 3) enclosed - пространство находящиеся между двумя пространствами (между global и local)

# enclosed - она возникает тогда, когда есть вложенность в функции 

# x = 'глобальна область видимости'

# def some_func():
#     x = 'это enclosed  область видимости'
#     print(x)
    
#     def some_func2():
#         x = 'это локальная область видимости'
#         print(x)

#     some_func2()
# print(x)
# some_func()


# def func():
#     a = 'func'   # ---- enclosed пространство
#     def inner_func():
#         a = 'inner_func'   # ----- local пронстранство
#         print(locals)
#     inner_func()
#     print(locals())

# func()
# print(globals())


# ====================================================================================


# 4) local - локальное пронстранство имен 

# по мене выполнения программы python создает разные пронстранства имен и удаляет их 


# def hello():
#     a = 'hello world'
#     print(locals())
#     print(a)

# hello()
# print(locals())



# def func(b, c):
#     a = 4
#     print(locals())

# func(2,3)

# print(locals())


# ===========================
# порядок поуска переменных 

# local -> enclosed -> global -> builtins 



# ====================tast 


# count = 0

# def counter():

#     global count
#     count += 1
#     print(count)

# counter()
# counter()



# def counter1():
#     try:
#         print(count)
#         count += 1
#     except:
#         print('f')

# counter1()
# counter1()




# def outer_function():
#     global a
#     a = 20

#     def inner_function():
#         global a
#         a = 30
#         print('inner function a = ', a)
#     inner_function()
#     print('outer function a = ', a)

# a = 40

# outer_function()



# def func():
#     a = '1'
#     def inner_func():
#         def inner_func2():
#             nonlocal a
#             a = 2
#         inner_func2()
#     inner_func()
#     print(a)

# func()



# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 'edited enclosed x'
#         print(x, 'is local')
#     local()
#     print(x, 'is enclosed')

# enclosed()



# def func():
#     var = 100
#     def nested():
#         nonlocal var
#         var += 100
#     nested()
#     print(var)

# func()



# def count(i):
#     counter = 0

#     def add():
#         nonlocal counter
#         print(counter)
#         counter += 1
    
#     for x in range(i+1):
#         add()

# count(10)



# обычно nonlocal позволяет нам назначать перменные во внешней области, но не в глобальной 



# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 30
#         def inner():
#             nonlocal x
#             x = 'Edited x'
#             print(x, 'inner()')
#         inner()
#     local()
#     print(x, 'enclosed ')

# enclosed()



# ========================================Tusk  ==============

# import random

# words = ['список', 'печатать', 'количество', 'программирование', 'виселица', 'семь смертных грехов']
# geas_try = 3

# def whil():
#     global word
#     word = random.choice(words)


# whil()

# blur_word = '*'*len(word)


# while True:
#     print('Печатается: ', blur_word)
#     print(f'Попыток осталось: {geas_try}')

#     letter = input('Введите одну букту для разгадки слово: ')

#     index = [i for i, c in enumerate(word) if c == letter]
    
#     for i in index:
#         res = list(blur_word)
#         res[i] = letter
#         ress = ''.join(res)
#         blur_word = ress
        
#     if not letter in list(word):
#             geas_try -= 1
#             if geas_try == 0:
#                 print('Вы потратели все попытке ;(', geas_try)
#                 break
#     elif blur_word == word:

#         print('Поздравляю вы угадали расшифровали слово!!!')
#         win = 'победа'
#         break

        
        
# string = 'tonaisuu'
# position = 6
# new_character = 'r'
# temp = list(string)            ============================== USFULL STRING
# temp[position] = new_character
# string = "".join(temp)
# print(string)


# var = 'переменная в foo' 
# def foo(): 
#     global var 
#     var = 'переменная foo' 
#     print('переменная в foo: ', var) 
#     def bar(): 
#         global var 
#         var = 'переменная bar' 
#     bar() 
# foo() 
# print('переменная в foo: ', var)4




# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}


# def post(let:dict):

#     for l,nl in let.items():
#         if nl >= 17:
#             print(f'{l}, Вы можете войти в клуб')
#         else:
#             print(f'{l}, извините, Вы не проходите по age-control')

# post(a)



# a = ['pipi', 'papa', 'mama']
 
# b = [i.title() for i in a]

# print(b)




# def count_symbols(strin:str):
#     glas = 'аоуыэяёюие'
#     soglas = 'нмлрйбвгджзпфктшсхцчщ'
#     left = 'ъь '
#     count_g = 0
#     count_s = 0
#     count_l = 0
#     for i in strin:
#         if i.lower() in glas:
#             count_g += 1
#         elif i.lower() in soglas:
#             count_s += 1
#         elif i.lower() in left:
#             count_l += 1

#     return (f'Количество гласных: {count_g}, согласных: {count_s}, остальных символов: {count_l}')


# print(count_symbols('Ырыскелди'))


# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def lower_7():
#     global a
#     ar = []
#     for i in a:
#         if i < 7:
#             ar.append(i)
#     return ar
    
    
# print(lower_7())