
# def decor_func(func):
#     print('Decor func')
#     return func()



# def func2():
#     print('func2')
#     return 'hello'

# def func3():
#     print('func3')
#     return 'world'

# res = decor_func(func2)
# print(res)
# res1 = decor_func(func3)
# print(res1)



# ДЕКОРАТОРЫ  - это функция котораый в свою очередь принимает другую функцию
# ДЕКОРАТОРЫ является функцией высшего порядка - это функции которые могут принять как аргумент любую функцию и вернуть ее 
# Декоратор  модифицирует и улучшает принятую функцию и выдает измененую 



# def func2(func):
#     print('Я буду работать до функции func1')
#     print(func())


# def func1():
#     return 'функция func2 завершилась'

# func2(func1)


# def upper_func(func):
#     def wrapper():
#         original_res = func().upper()
#         # modified_res = original_res.upper()
#         # return modified_res
#         return original_res
#     return wrapper

# @upper_func
# def some_text():
#     return 'Hello World'


# @upper_func
# def some_text1():
#     return 'Hello Union'


# res = upper_func(some_text)
# print(res())

# print(some_text1())

# print(some_text())




# def get_name(name):
#     return name

# def get_age(age):
#     return age

# def get_last_name(last_name):
#     return last_name


# print(get_name('RyuDzaky'))
# print(get_age(23))
# print(get_last_name('Junior'))


# def decorator_func(func):
#     def wrapper(some_info):
#         return 'Вы передали: ' + str(func(some_info))
#     return wrapper


# @decorator_func
# def get_name(name):
#     return name

# @decorator_func
# def get_age(age):
#     return age

# @decorator_func
# def get_last_name(last_name):
#     return last_name


# print(get_name('RyuDzaky'))
# print(get_age(23))
# print(get_last_name('Junior'))




# def func_def(function_to_decorate):  # сюда попадает функция которую нужно задекорировать
#     def wrapper():        # оберточная оболочка для функции
#         print('Я код, который отрабатывает до вызова функции!!!')
#         function_to_decorate()
#         print('А я кот который сработает после!!!')
#     return wrapper     # возвращаем обертку


# @func_def
# def func1():    # функция которую мы задекорируем
#     print('Я функцию func1')


# res = func_def(func1)
# print(res())

# func1()




# если мы используем аргументы у функции, то мы обзательно должны передавать их в декоратор 

# def decorator(func):

#     def wrapper(arg):
#         print(f'Смотри что я принимаю {arg}')
#         func(arg)
#     return wrapper

# @decorator
# def func1(word):
#     print(f'Я принимаю в себя слово {word}')

# func1('RyuDzaky')





# def decorator(func):   # лучше использовать такую запись, она является универсальной для всех функций
#     def wrapper(*args,**kwargs):
#         print(f'Здесь args {args}')
#         print(f'Здесь kwargs {kwargs}')
#         func(*args,**kwargs)
#     return wrapper

# @decorator
# def func_without_parametrs():
#     print('Здесь функция без параметров\n')

# @decorator
# def func_with_parametrs(first_name, last_name):
#     print('Здесь функция с параметрами')
#     print(f'Hello {first_name} {last_name}\n')

# @decorator
# def func_with_parametrs_kwargs(first_name, last_name):
#     print('Здесь функция с параметрами')
#     print(f'Hello {first_name} {last_name}')


# func_without_parametrs()
# func_with_parametrs('Ryu', 'Dzary')
# func_with_parametrs_kwargs(frist_name='Ryu', last_name='Dzary')




# def div(func):
#     print('f1')
#     def wrapper(*args,**kwargs):
#         print(func.__name__)
#         return '<div>' + func(*args, **kwargs) + "</div>"
#     return wrapper

# @div
# def get(name, last_name):
#     print('f2')
#     return name + last_name

# print(get('Ryu', 'Dzaky'))




# def bread(func):
#     def wrapper(*args, **kwargs):
#         return 'bread' + str(func(*args, **kwargs)) + 'bread'
    
#     return wrapper


# def ingridients(func):
#     def wrapper(*args, **kwargs):
#         return 'tomato' + str(func(*args, **kwargs)) + 'salad'
    
#     return wrapper

# @bread
# @ingridients
# def get_sandwich(x):
#     print(x)
#     return x

# print(get_sandwich('sasuges'))

# res = ingridients(get_sandwich('sasuges'))
# res1 = bread(res)



# def decorator_maker(f):
#     print(f)
#     print('Я создаю декораторы')
#     def my_decorator(func):
#         print('Я декоратор, я буду вызван в момент декорации функции')
#         def wrapper():
#             print('Я функция обертка, вызываюсь каздый раз при декорирований функции')
#             return func()
#         print('Я возвращаю обернутую функцию')
#         return wrapper
#     return my_decorator


# @decorator_maker(2)

# def decorate_function():
#     print('Я депорированная функция')

# decorate_function()





# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Функция отработала : {end - start}')
#     return wrapper


# @benchmark
# def call_webpage():
#     import requests
#     webpage = requests.get('https://google.com')


# @benchmark
# def iterate_list():
#     for i in range(50000):
#         print(i)

# call_webpage()
# iterate_list()



# def repeat(num):
#     def goll(gol):
#         def wrapper(func):
#             for i in range(0, num):
#                 print(func)
#         return wrapper
#     return goll

# @repeat(num = 4)
# def function(name):
    
#     print(f'{name}')

# function('RyuDzaky')




# def countdown(seconds):
#     res = []
    
#     def goll(gol):
#         def wrapper(func):
#             for i in range(1, seconds+1):
#                 res.append(i)
#                 if i == seconds:
#                     res.reverse()
#             for k in res:

#                 print(k)
#             if i == seconds:
#                 gol()

#         return wrapper
#     return goll

# @countdown(seconds=5)

# def func():
#     print('Hello world')

# func('s')