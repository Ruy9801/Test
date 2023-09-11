# list - изменяемый, индексируемый, упорядоченный (хранит порядок вставки в него элементов) итерируемый тип данных
# итерируемый обьект - это обьект в котором можно пройтись по каждому элементу (for)

# lisst = []
# list() 

# list_ = [1,2,3, 'hello', [5, 1.2], {'a': 3}]
# print(list_[1])
# print(list_[4][0]) #list_[4] --[0,1.2] --[0]


# names = input('Enter names with spaces: ').lower().split()
# guest = input('Enter your name: ').lower()

# print(names) # ['name', 'name', 'name']


# if guest in names:
#     print('Yes')
# else:
#     print('No')


# my_list = list('hello world')
# print(my_list)


# range() - возвращает последовательносит элементов
# range(0,10) -- создай список числе от 1 до 10, 10 не включается в список

# my_list = list(range(10,2,-1))

# []
# my_list = [1_000_000_000_000]
# print(my_list)

# list3 = [1] * 5
# print(list3)



# Методы списка

# list_ = ['string', 2, 3, 4, 5]
# del list_[0]
# print(list_)
# list_[0] = 1
# print(list_)


# append - добовляет элемент в конец списка и принимает в себя один элемент

# list_ = []
# list_.append(1)
# print(list_)
# list_.append('string')
# list_.append([1,2,3,4,5])
# print(list_)


# extend(element) - расшираяет список добовляя в конец элементы

# list_ = [1,5]
# list_.extend('hello')
# print(list_)

# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)

# print(list1)


# insert(index,element) - допавляет элемент по указанному индексу

# list1 = [1,2,3]
# last_index = len(list1) + 1
# list1.insert(100,'hello')
# print(list1)


# index(element,start,end) - возвращает индекс элемента

# list_ = [1,2,3,4,5, 6, 7]
# result = list_.index(2,3)
# print(result)


# clear - очищает список

# list_ = [1,2,3,4,5]
# print(list_.clear())


# count - считает количество принятого элемента в списке

# list1 = ['hello',1,2,3,4,5,6,7,8]
# print(list1.count(1))

# len() - считает длину обектов
# list_ = [1,2,[1,3,4],4]
# print(len(list_))


# pop - удаляет элемент по индексу и возвращает его, если индекс не указан, то удаляет последний элемент

# list_ = [1,2,3,4,5]
# popped = list_.pop(1)
# print(list_)
# print(popped)

# remove - удаляет первый принятый элемент в списке

# list_ = [1,2,3,4,5,6]
# removed = list_.remove(1)
# print(list_)
# print(removed)


# reverse = изменяет список расставяя его элементы в обратном порядке

# list_ = [1,2,3,4,5]
# list_.reverse()
# list1 = list_.copy()
# print(list_)


# sort - сортирует список состоящий из элементов одного типа данных в возрастающем порядке(в алфавитном для строк) 
# Если указан reverse=True то список будет отфильтрован в убывающем порядке

# list1 = [1,2,3,4,5,12,22,32,55,54]
# list1.sort(reverse=True)
# print(list1)

# list_ = ['f', 'a', 'b', 's', 'E', 'n']
# list_.sort()
# print(list_)

# list1 = [1,2, 'hello']
# list1.sort()
# print(list1)


# copy = копирует список

# list_ = [1,2,3,4,5,[2,3,4]]
# new_list = list_.copy()
# print(new_list)


# цикл - это блок кода который повторяется несколько раз мы используем цкл в тех случаях, когда нам нужно повторить что нибудь n когличество раз

# for - цикл, который работает с итрируемым объектом
# list str tuple 

# интерируемый обьект - обьект по которому можно проходиться, который способен возвращать элемент по одному

# a = 0 
# for i in a:
#     print(i) 
# Error


# string = 'string'

# for i in string:
#     print(i)

# for элемент in итеруемый обьект

# list1 = [1,2,3,4,5]

# string = 'string'

# for element in string:
#     print(element)


# for i in range(5):
#     print(i)

# for element in 12345:
#     print(element)    - Error



# for i in range(10):
#     if i == 2:
#          print(i)


# for i in range(10):
#     print(i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             print(5,'j')
    
#     if i == 3:
#         print(2, 'i')

# инкремент - это увеличение значений какой либо переменной
# дикримент - это увеличение значений какой либо переменной

# инкримент

# a = 0
# a = a + 1
# a += 1 равноценно a = a + 1
# print(a)

# дикремент





# ===================Dayly test====================

# list1 = [1,2,3,4,5,6,22,33,23,12]
# even=[]
# odd=[]
# for ch in list1:
#     print(ch)
#     if ch % 2 == 0:
#         even.append(ch)
#     else:
#         odd.append(ch)
    
# print(even)
# print(odd)


# list1 = [1,2,3,4,5]
# res = 0
# for re in list1:
#     res += re
    
    
# print(res)




# ======================== 1

# number = [2, 3, 5, 2, 5, 6, 7]
# number = input('Введите цифры через запятую: ').split()

# number1 = number[0],number[-1]
# number2 = number, number.pop(-1), number.insert(100,'Makers')

# print(number1)
# print(number2)


# ============================== 2

# import random

# n1 = random.randint(1, 10)
# n2 = random.randint(1, 10)
# n3 = random.randint(1, 10)
# n4 = random.randint(1, 10)
# n5 = random.randint(1, 10)
# n6 = random.randint(1, 10)
# n11 = random.randint(1, 10)
# n12 = random.randint(1, 10)
# n13 = random.randint(1, 10)
# n14 = random.randint(1, 10)

# number1 = n1, n2, n3, n4, n5, n6, n11, n12, n13, n14
# number = [n1, n2, n3, n4, n5, n6, n11, n12, n13, n14]
# number.sort()

# print(number1)
# print(number)

# ===================================== 3

# word = input('Введите ваш списак слов: ').split()
# print(word)


# for wl in word:
#     wordl = len(wl)


# print(wordl)



# ======================= своя 

# numbers1 = []
# numbers2 = list()

# print(type(numbers1))
# print(type(numbers2))

# numbers4 = [1, 2, 3, 5]
# numbers5 = list(['Maker', 'bootcamp', True, 43])
# print(numbers5)

# numbers = [3, 3, 3, 3, 3]
# numbers2 = [3] * 6
# print(numbers)
# print(numbers2)


# range(end)
# number = list(range(10))
# print(number)

# range(start,end)
# number = list(range(1, 10))
# print(number)

# range(start,end,step)
# number = list(range(1, 10, 2))
# print(number)
# numbers = list(range(10,0,-1))
# print(numbers)

# for i in range(1,11):
#     print(i**2)

# =========сравнение списков===========

# number1 = [1, 2, 3, 4, 5]
# number2 = [1, 2, 3, 4, 5]

# print(number1 == number2)


# numbers = [1, True, 'Makers', 'hello', 2.3, (1, 3), ['hell']]

# =============индексация=============

# numbers = [1, True, 'Makers', 'hello', 2.3, (1, 3), ['hell']]

# print(numbers[2])
# print(numbers[1])
# print(numbers[-1])
# print(numbers[4])

# numbers = [1, True, 'Makers', 'hello', 2.3, (1, 3), ['hell']]

# numbers[0] = 2
# print(numbers[0])

# users = ['Alice', 'Sam', 'Carl']

# for user in users:
#     print(f'hello {user}')

# for letter in 'Makers':
#     print(letter.upper())


# s='hello'
# s[:len(s)//2]


# ==================== Task 3

# name_of_list = ['RyuDzasky']

# nelist = str(name_of_list)
# new_list = list(nelist[2:-2])
# num = int(len(new_list ) / 2)

# if int(len(new_list ))%2 != 0:
#     print(new_list [(num + 1):] + new_list [:(num + 1)])
# else:
#     print(new_list [num:] + new_list [:num])



# suitcase = []

# suitcase.append('skarf')
# suitcase.append('boll')
# suitcase.append('gun')
# suitcase.append('buttle')
# suitcase.append('phon')
# suitcase.pop()

# suitcase.insert(0,'kok')

# print(suitcase)



# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# res = []
# for num in nums:
#     if num < 5:
#         res.append(num)
        

# print(res)        


# here = input().split(',')


# list_ = here

# tuple_ = tuple(here)

# print(list_)
# print(tuple_)



# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for mm in list_:
#     new_list.append(str(mm))


# print(new_list)




# list_ = [1, 2, 3, 4, 5]

# new_list = []

# for mm in list_:
#     if mm%2==0:
#         new_list.append(str('четное'))
#     elif mm%2!=0:
#         new_list.append(str('нечетное'))

# print(new_list)



# list_= []
# for mm in range(20):
#     list_.append(int(mm))
# print(list_)


# list_ = []

# for mm in range(0,101,2):
#     list_.append(int(mm))

# print(list_)




# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# list3 = []
# list4 = 0

# for i in list1:
#     list3.append(int(i))
# for i in list2:
#     list3.append(int(i))
# for i in list3:
#     list4 += int(i)

# print(list4)



# numbers = 43,2,43,234
# num = input('enter num: ').split(',') 
# list_ = [] 

# for i in num: 
#     list_.append(i) 
#     list_.sort() 

# print(list_)




# list_ = [1, 2, 3]
# set_ = set(list_)

# if len(set_) != len(list_):
#     print('yes')
# else:
#     print('ERROR')




# list_ = []

# for i in range(55,9184,5):
#     list_.append(int(i))

# print(list_)




# list_ = [20, 10, 20, 1, 100]

# min_number = 0

# list_.sort()
# min_number = list_[0]

# print(min_number)



# tuples = [(), ('ram', '15', '8'), (), ('lasman', 'sita')]
# res = []
# for mm in tuples:
#     if len(mm) > 0:
#         res.append(mm)

# print(res)



# name1 = input().split()
# name2 = input().split()
# name3 = input().split()
# name4 = input().split()
# name5 = input().split()

# names = []


# if len(name1)> 2:

#     names.append(str(name1[2]))
# elif len(name1) <= 2:

#     names.append(str(name1[1]))

# if len(name2)> 2:

#     names.append(str(name2[2]))
# elif len(name2) <= 2:

#     names.append(str(name2[1]))

# if len(name3)> 2:

#     names.append(str(name3[2]))
# elif len(name3) <= 2:

#     names.append(str(name3[1]))

# if len(name4)> 2:

#     names.append(str(name4[2]))
# elif len(name4) <= 2:

#     names.append(str(name4[1]))

# if len(name5)> 2:

#     names.append(str(name5[2]))
# elif len(name5) <= 2:

#     names.append(str(name5[1]))
    
# names.sort()
# print(names)




# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]

# number = 8
# res = 0
# for mm in list_:
#     if mm == number:
#         res += 1

# print(res)





# list_ = [1, 'abcd', 3, '1', 4, 'xys', 3, 'oib', 8, 7, 18]

# dig = []

# for i in list_:
#     if type(i) == int or i.isdigit():
#         dig.append(int(i))

# print(sum(dig))

# num = 5

# if num <= 0 and num >12:
#   print("Такого месяца нет!")
# elif num == 12 or num == 1 or num == 2:
#   print('зима')
# elif num == 3 or num == 4 or num == 5:
#   print('весна')
# elif num == 6 or num == 7 or num == 8:
#   print('лето')
# elif num == 9 or num == 10 or num == 11:
#   print('осень')