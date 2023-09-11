# исключения и ошибки - обьекты, которые прерывают работу кода 

# ошибки --= проблема в синтаксисе (которые мы исправляем самостоятельно)

# 1. SyntaxError: забыли элемент где-то , неправильно назвали переменную, забыли литералы у функций и модулей

# 2. IndentationError: ошибка табуляции просто нажимай Tab где нужна 

# 3. TabError: неверная табуляция (смешивание пробелов и табов) 



# исключения --= это код написан верно, но программа работает не так как ожидалось 

# 1. ZeroDivisionError --= выходит при делении на ноль print(23 / 0) /,//,% на 0

# 2. NameError --= исключение выходит, когда мы обращаемся к несуществующей переменной

# 3. IndexError --=  исключение которые выходит, когда обращаемся к несуществующему индексу

# 4. KeyError --=  исключение которое выходит когда мы обращаемся к несуществующему ключу

# 5. ImportError --= исключение которое выходит когда мы импортируем не сущиствующий библиотеку

# 6. ValueError --= когда функцию передаем не тот тип данных

# 7. TypeError --= когда мы пытаемся использовать методы не свойственны какому то типу данных либо же когда мы передаем в функцию больше или меньше аргументов чем она ожидает футкцию

# 8. AttributeError --= выходит когда мы обращяемся к несуществующему аттрибуту или методу обьекта

# 9. BaseException() --= прородитель(все ошибки)




# try except - мы используем это строение чтобы наш код не прекращал работу 

# try:
#     код который может вызвать ошибку
# except:
#     код который сработает если в try вышла ошибка
# else:
#     код который сработает если в try  не вышла ошибка
# finally:
#     код который сработает в любом случае



# try:
#     age = int(input('Введите возраст: '))
# except (ValueError, TypeError):
#     age = int(input('Введите возраст еще раз: '))

# print(age)


# try:
#     a = 2
#     b = 0
#     result = a/b
# except ZeroDivisionError:
#     print('error')



# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')



# try:
#     int('f')
# except ValueError:
#     print('Неверный код')
#     try:
#         3/0
#     except ZeroDivisionError:
#         print('Деление на ноль')




# try:
#     num1  = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     print(num1/num2)
# except (ZeroDivisionError, ValueError):
#     print('Произошла ошибка!')



# try:
#     dict_ = {k: k**2 for k in range(1000) if k%a==0}
# except NameError:
#     print('Переменной а нет')
#     a = int(input('Укажите число: '))
#     dict_ = {k: k**2 for k in range(1000) if k%a==0}
#     print(dict_)
#     try:
#         a = int(input('Укажите число: '))
#         dict_ = {k: k**2 for k in range(1000) if k%a==0}
#         print(dict_)
#     except ValueError:
#         print('а должно быть числом')
#         dict_ = {k: k**2 for k in range(1000) if k%a==0}
#         print(dict_)


# try:
#     num1 = int(input('enter number: '))
#     num2 = int(input('enter number: '))
#     result = num1/num2
#     print(result)
# except ValueError:
#     print('Ты ввел неправильные данные')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')


# dict_ = {'a': 5, 'b': 10, 'c': 15, 'd': 20}

# try:
#     key=input('enter key: ')
#     value = dict_[key]
#     print(value)
# except KeyError:
#     print('Нет такого ключа!')
# else:
#     value *= value
#     print(value,'block else')



# try:
#     result = a*2
#     print(result)
# except Exception as e:
#     print(f'Возникла {e.__class__}')
# finally:
#     a = 5
#     result = a*2
#     print(result, 'block finally')




# raise -= искуственно вызывает ошибку 

# number = int(input('enter: '))

# if number>5:
#     raise 'значение не должно быть больше 5!'




# age = 20

# if age>18:
#     raise Exception('Error')
    



# try:
#     if 2 > 1:
#         raise ValueError
# except ValueError:
#     print('Возраст больше 2')




# element1 = input('Введите чтота: ')
# element2 = input('Введите чтота: ')

# if element1.isdigit() and element2.isdigit():
#     res = int(element1) + int(element2)
#     print(res)
# else:
#     print(element1+element2)



# user = input('Введите пользовательское имя: ')
# username = 'RyuDzaky'
# ID = 3
# dict1 = {ID: username}

# try:
#     for k,v in dict1.items():
#         if v==user:
#             print(f'ID {k}')
#             print(f'Hello my dear freand {v}')
#             print('Спасибо')
#         else:
#             raise ValueError
# except ValueError:
#     print('Введенного юзера нет в базе данных')
#     print('Спасибо!')




# age = int(input('Введите ваш возраст: '))

# try:
#     raise ValueError
# except ValueError:
#     if age <= 0:
#         print('Ваш возраст должен быть больше 0')



# try:
#     def filter_comment(comment:str,banlist:[])-> None: 
        
#         comment1 = comment.replace('.','').replace('!','').replace('?','').replace(',','').lower()
        
#         for i in banlist:

#             if i in comment1:
#                 raise ValueError('Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст')
# except ValueError:
#     pass
    
# filter_comment('Hello, world', ['hello'])
# filter_comment('HelloWorld', ['hello']) 
# filter_comment('ochocientos ochenta y ocho')
# filter_comment('I love this recipe', ['hate', 'unlike', 'liken\'t'])
# filter_comment('Dis? recipe. is i !!UNLike!?!! really much!', ['hate', 'unlike', 'liken\'t']) 