# list_ = ['abc',1,2,3]

# count = 0

# for i in list_:
#     count+=1
# print(count)



# str_ = 'string'

# count = 0

# for i in str_:
#     count += 1
# print(count)



# def my_len(res):
#     count = 0
#     for i in res:
#         count += 1
#     print(count)           -== Usfull

# str_ = 'string'
# list_ = ['abs',1,2,3]

# my_len(str_)
# my_len(list_)

# функции - это именованный блок кода, который выполняет одну задачу и может принимать в себя оркументы и возвращать какое то значение 
# футкцию можно вызывать много раз, обращаясь по имени


# def - ключевое слово, указывает  python что мы хотим создать функцию
# название функции = это переменная, под этим имененем питон запоминает название этой функции
# скобки - нужный для того, чтобы функция могла принимать параметры


# синтаксис

# def название_функции(агрументы):
    # принимает аргументы для работы в теле название_функции
    # тело функции 

# название_функции(агрументы)


# def my_sum(x,y):
#     print(x+y)
#     return x+y

# my_sum(2,2)
# my_sum('Ryu','Dzaky')
# my_sum(9,0)

# res = my_sum(4,5)
# print(res)



# return - используется для возвращения результата и на этом моменте функция завершает свою работу

# return - это ключевое слово, которое дает понять python что за этой командой будет какя то информация которая является окончательный результатом нашей функции 


# def sum_two_numver(a,v,s):
#     print(a,v,s)

# sum_two_numver(5,3) # TypeError: sum_two_numver() missing 1 required positional argument: 's'


# def sum_two_numver(a,v,s=9):
#      print(a,v,s)

# sum_two_numver(2,3)   # позиционные аргументы
# sum_two_numver(a=2,v=3,s=9)  # - Именованные аргументы



# распаковка list(*), dict(**)

# list1 = list(range(1,11))
# print(list1)
# list1 = [*range(1,11)]  # Распаковываем значение в новый список
# print(list1)


# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {**dict1}
# list3 = [*dict1]
# print(dict2)
# print(list3)



# необязательные оргументы args kwargs 
# args -= принимает позиционные аргументы 
# kwargs -= принимает именнованные аргументы 

# args - tuple 
# kwargs - dict 

# def two_sum(a,b, *args, **kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)
#     return a+b+sum(args) +sum(kwargs.values())

# res = two_sum(2,3,6,9,92,29,39,2,34,5,6,first = 400,second=30)

# print(res)



# def func(a,b=10,*args,**kwargs):
#     print('a',a)
#     print('b',b)
#     print('args -- ',args)
#     print('kwargs -- ', kwargs)

# func(5,3,9,2,'you',kk = 23, vv = 24)

# func(1,c=3,b='df',v=23)



# аннотация - делает код более информативным 


# num: int = 10
# str_: str = 'Hello'


# def func(a,b:str,c:int) ->int :
#     """
#     Заметка как работает функция
#     """
#     print(a+b+c)

# func(1,'str',2)




# list_ = ['olo','lol','hello','world','aziza']

# def palindrom(words:list) -> list:
#     palindrom1 = []
#     for word in words:
#         if word == word[::-1]:
#             palindrom1.append(word)
#         else:
#             continue
#     return palindrom1  # После return ничего не выходит
#     print('Вернии!!!')

# print(palindrom(list_))



# dict1 = {'a': 1, 'b': 2, 'c': None, 'e': 3, 'd': None}

# def funk(key:dict):
#     res = {}
#     for k,v in key.items():
#         if v==None:
#             pass
#         else:
#             res.setdefault(k,v)
#     return res

# print(funk(dict1))



# def valemail(email:str):
#     indx = email.find('@')
#     domains = ['gmail.com','mail.ru']
#     if "@" not in email:
#         raise Exception('Invalid email')
#     elif not email[0:indx]:
#         raise Exception('Invalid email')
#     elif email[indx+1:] not in domains:
#         raise Exception(f'Invalid email domain {domains}')
#     print('Emailis valid and successfully saved')
#     return True

# email = 'rysa@gmail.com'
# # print(valemail(email))



# def ragister(email:str, passwerd1:str, passwerd2:str):
#     db_email = None
#     password = None
#     if valemail(email):
#         db_email = email
#     if passwerd1 != passwerd2:
#         raise Exception('пароли не совпадают')
#     password = passwerd1
#     msg = 'Вы успешно зарегистрировались'
#     return {'email': email, 'password': password, 'msg': msg}

# email = 'rysa@gmail.com'

# passwerd1 = 'rysa9888'
# passwerd2 = 'rysa9888'

# print(ragister(email=email, passwerd1=passwerd1, passwerd2=passwerd2))



# ======================Tasks=================

# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))

# def res(a,b):
#     num = a+b
#     print(num)
#     return num

# res(num1,num2)

# string = input('Enter string: ')

# def res(string:str):
#     str_len = len(string)
#     print(str_len)

# res(string)



# def res(a,b):
#     type1 = type(a)
#     type2 = type(b)
#     print(type1, type2)

# res('RyuDaky', 988)


# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))

# def res(a,b):
#     num = a/b
#     print(num)

# res(num1,num2)



# dict1 = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 

# def res(key:dict):
#     for k,v in key.items():
#         print(k)

# res(dict1)


# num = int(input('Enter num: '))

# def res(n:int):
#     if n%2==0:
#         print("It's odd number")
#     else:
#         print("It's even number")

# res(num)


# string = input("Enter something: ")

# def res(st:str):
#     word = st.replace(' ','')
#     if word.lower() == word[::-1].lower():
#         print('Введённое слово является палиндромом!')
#     else:
#         print('Введённое слово не является палнидромом!')

# res(string)



# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))

# def res(n1:int,n2:int):
#     if n1 > n2:
#         print(f'{n1} больше')
#     elif n1 < n2:
#         print(f'{n2} больше')
#     else:
#         print('Они равны!')

# res(num1,num2)


# num = list(input('Enter numbers: '))

# def res(nums:list):
#     num_sum = 1
    
#     for i in nums:
#         if i.isdigit():
#             num_sum *= int(i)
#     print(num_sum)

# res(num)



# num = input('Enter numbers: ')

# def res(nums:str):

#     num_sum = 0
    
#     for i in nums:
#         if i.isdigit():
#             num_sum += int(i)
#     print(num_sum)

# res(num)



# num = int(input('Enter number: '))
# def nums(num1:int):
#     for i in range(1,num1+1):

#         if num1%2==0 and num1!=2:
#             return('Натуральное число')  
#         elif num1%num1==0 and num1%1==0:
#             return('Простое число')
    
    
# print(nums(num))



# list1 = [1, 4, 6, 2, 1, 3, 6, 8, 2, 6, 7]

# def res(list_:list) -> list:
#     list_ = list(set(list_))
#     list_.sort(reverse=True)
#     return list_


# print(res(list1))




# num1 = int(input('Enber number: '))
# num2 = int(input('Enter number2: '))

# def sum_range(start:int,end:int):
#     summ = 0
#     if start<end:
#         for i in range(start,end+1):
#             summ+=i
#     else:
#         for i in range(end,start+1):
#             summ+=i
#     return summ

# print(sum_range(num1,num2))



# num1 = int(input('Enber number: '))
# num2 = int(input('Enter number2: '))

# def sum_range(start:int,end:int):
#     if start > end:
#         start, end = end, start
#     return sum([i for i in range(start, end + 1)])

# print(sum_range(num1,num2))



# def fuc(list_=[]):
#     res = []
#     res.append(list_)
#     return res

# print(fuc('kjs'))


# def get_sum(num: int) -> int:
     
#     dict_ = []

#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             dict_.append(i)

#     return dict_

# print(get_sum(1098))



# ===================Tusks==============
# import random

# name = input('Введите имя и фамилию: ')

# def get_info(info:str) -> str:

#     part1 = info.replace(' ','')
#     generate_password(part1)
    
# def generate_password(password:str) -> str:

#     part2 = random.randint(1000000,9999999)
#     part3 = password + str(part2)
#     print(part3)


# get_info(name)



        
# operator = input("enter operator + - / *: ")
# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))

# def get_data(num11:int, num22:int , oper:str):
    
#     if operator == "+":
#         res = num1 + num2
#         return res
#     elif operator == "-":
#         res = num1 - num2
#         return res
#     elif operator == "*":
#         res = num1 * num2
#         return res
#     elif operator == "/":
#         res = num1 / num2
#         return res
    
# resss = get_data(num1,num2,operator)


# def result(ress:int):
#     print(ress)

# result(resss)    




# def calc(num1: int, num2: int, oper:str):
#     if oper == '+':
#         add_(num1, num2)
#     elif oper == '-':
#         sub_(num1, num2)
#     elif oper == '/':
#         div_(num1, num2)
#     elif oper == '*':
#         mult_(num1, num2)

# def add_(num1: int, num2: int):
#     res = num1 + num2
#     print(res)

# def sub_(num1: int, num2: int):
#     res = num1 - num2
#     print(res)

# def div_(num1: int, num2: int):
#     res = num1 / num2
#     print(res)

# def mult_(num1: int, num2: int):
#     res = num1 * num2
#     print(res)

# calc(2,3,'+')



# def add_(num1: int, num2: int):
#     return num1 + num2
    
# def sub_(num1: int, num2: int):
#     return num1 - num2
    
# def div_(num1: int, num2: int):
#     return num1 / num2

# def mult_(num1: int, num2: int):
#     return num1 * num2
    
# def result(num1: int, num2: int, oper):
#     if str(oper) == '+':
#         return add_(num1, num2)
#     elif str(oper) == '-':
#         return sub_(num1, num2)
#     elif str(oper) == '/':
#         return div_(num1, num2)
#     elif str(oper) == '*':
#         return mult_(num1, num2)

# result(2,3,'+')





# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]


# def func17(list1:list):
#     list2 = []
#     for i in list1:
#         i['salary'] = i['overTime']*200+i['salary']
#         i.pop('overTime')
#         list2.append(i)

#     return list2

# print(func17(employees))


 


# balance = 2000



# def spent(stuf, spent:int):
#     global balance
#     res = {}
    
#     if spent <= balance:
#         balance -= spent
#         part = {'target': stuf, 'spend': spent}
#         res.update(part)
#     elif spent > balance:
#         print('Ваш кашелек истащен XO')

#     return res



# def deposit(depo:int):
#     global balance
#     balance += depo
#     print(balance)

# print(spent('Anime', 200))
# deposit(800)



# balance = 2000


# def spent(stuf, spent:int, balan:int):
#     global balance
#     res = {}
    
#     if spent <= balan:
#         balance -= spent
#         part = {'target': stuf, 'spend': spent}
#         res.update(part)
#     elif spent > balan:
#         print('Ваш кашелек истащен XO')

#     return res


# def deposit(depo:int):
#     global balance
#     balance += depo
#     return balance
    

    
# res = spent('Anime', 200, balance), deposit(800)
# print(res)