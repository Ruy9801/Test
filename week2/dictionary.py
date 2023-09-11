# Тип данных словаки (dict) 

# словари - это одна из наиболее часто используемых структук данных, позволяющий хранить обекты
# словарь - изменяемый, итерируемый, неиндуксируемый, упорядоченный тип данных в котором элементы храняться в виде пары ключ значение


# {} - литералы

# dct = {}
# print(type(dct))

# dict_ = {'a': 'hello', 'b':2, 'c':3}

# dict_ = {{'s':5}:5} - None
# print(dict_)

# dict1 = {1:'hello', 2:[1,2,3,4], 4.5:{'a':2}, (1,2,3): 'a'}
# print(dict1[1])

# dct = {'name': 'Jown', 'age': 25, 'hobby': ['fishing', 'footbal', 'dota'] }

# print(dct['hobby'])
# print(dct['hobby'][1])
# data = {'email': 'john@gmail.com', 'password': 'im1m2m333'}

# dict2 = dict([('key1', 'value1'), ('key2', 'value2')])
# print(dict2)

# dict3 = dict(['ab', 'cd','de'])
# print(dict3)


# dict4 = dict()
# dict4['key1'] = 'value1'
# print(dict4)


# dct = dict(age=25)
# print(dct)
# dct['age'] = 23
# print(dct)


# dct = {'age': True, 'age': 78}
# print(dct)


# dict.clear() - очищает словать

# dct = {'name': 'john', 'age': 25}
# dct.clear()
# print(dct)


# import copy

# copy() - возвращает копию словаря

# dct = {'name': 'Ryu', 'age': 18, 'hoppy': ['game', 'anime', 'diving']}
# dct2 = dct.copy()
# dct2['hoppy'][2] = 'hi'
# print(dct2)


# fromkeys[object, value] - создает словать с ключами из object и значием value для всех ключей если не передать value то значение у всех ключей будет None 

# list1 = ['name', 'age', 'hobby']
# dct = dict.fromkeys(list1, 'hi')
# print(dct)

# d = dict.fromkeys('a')
# print(d)

# методы получения элементов словаря

# get(key, default) - возвращает значение по этому ключу

# dct = {'name': 'Ryu', 'age':18}
# print(dct.get('age', 'нет такого ключа'))  # -- выдает None если нет такого ключа
# print(dct['age']) # -- выдает ошибку если такого ключа тен


# update - добавляет новый словарь в наш словарь

# dct = {'name': 'Jack', 'age': 18}
# new_dct = {'hobby': ['game', 'anime']}
# dct.update(new_dct)
# print(dct)


# setdefault - получение значений, работает точно также как get() но если такого ключа нет он создаст новую пару

# dct = {'name': 'Ryu', 'age': 18}
# dct.setdefault('hobby')
# print(dct)


# values() - выводит значение которое есть в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.values()))


# keys() - выводит ключи которые есть в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.keys()))


# items() - выводит все ключи и значение в словаре

# dct = {1: 2, 2: 1, 3: 4, 4: 3}
# print(list(dct.items()))


# pop(key, [message]) - удалет пару ключи и значение и возвращает значениею. если ключа нет то возвращает message (по умаолчанию приходит ошибка)


# dct = {'name': 'Ryu', 'age': 18}
# remove = dct.pop('name')
# print(remove)
# print(dct)


# popitem()  - удаляет и возвращает пару ключ значение удаляет последнюю добавленную пару

# dct = {'name': 'Ryu', 'age': 18}
# # dct['address'] = 'Bischkek'
# remove = dct.popitem()
# print(remove)

# ============================ Задачки =======================

# ==========================1

# dict_ = {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'd': 5, 'y': 6}

# for key,value in dict_.items():

#     if value%2==0:
#         dict_[key] = 0
        

# print(dict_)


# =========================2

# dict_ = {'hello': None, 'python': None, 'javascript': None, 'makers': None}

# for keyl in dict_.keys():
#     dict_[key] = len(keyl)

# print(dict_)


# ========================3

# dict_ = {'John': 60, 'Jack': 70, 'Anton': 85, 'Bake': 81, 'Nastya': 93}

# nums = 0
# for num in dict_.values():
#     nums += num

# number = nums / len(dict_)
# dict_['avarage'] = number
# print(dict_)        



# ====================== tasks 24 avgust

# ====================1

# university = {'программирование': 99, 'экономика': 50, 'медицина': 78}


# university['программирование'] = 23
# univer = {'лингвистика': 87}
# university.update(univer)
# university.pop('медицина')

# print(university)

# sumn = 0
# summ = []
# for i in university.values():
#     sumn += int(i)
    

# print(f'Колв учатнищихся: {sumn}')


# =======================2


# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# dict_swapped = {
# value: key

# for key,value in dict_.items()

# }

# print(dict_swapped)


# ======================3


# gest = int(input('Введите количество гостей которых хотите пригласить: '))

# gests = {}
# number = 0

# while True:
#     number +=1
#     gest1 = input('По одному введите имя гостей которые придут: ')
#     gests[number] = gest1
    
#     if len(gests) == gest: break


# print(gests)



# ========================4



# baylist = {1:'Помидор', 2:'Огурец', 3:'Молоко', 4:'Кефир', 5:'Банан'}

# print(f'Мне нужно купить: {baylist}')

# bayll = len(baylist)

# number = 0
# while len(baylist) != 0:

#     bayed = input("Я купил: ")
#     number += 1
#     if number == 5: break
#     for key,value in baylist.items():
#         if value == bayed:
#             baylist[key] = 0
            
        
        

# print(f'Пора расплататься в кассе Xd')

# for key,value in dict_.items():

#     if value%2==0:
#         dict_[key] = 0
        


# Задание 9
# Создайте словарь a с числовыми значениями. Создайте новый словарь b, такой же как словарь а, но все четные значения замените на 2.

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for k, v in a.items(): 
#     if v%2==0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
# print(b)




# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# c = {} 
# for k, v in a.items(): 
#     b = v / 5 
#     c.setdefault(k,b) 
# print(c)



# Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным (специальным методом) и распечатайте результат.

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()): 
#     if v % 2 == 0: 
#         del a[k] 
# print(a)



# В переменные a1 , a2 , a3 создайте любые словари тремя возможными способами.

# a1=dict(a=1, b=2, c=3) 
# a2=dict([('d', 4),('e', 5),('f', 6)]) 
# a3=dict([('a', 1)], b=2, c=3) 
# a4=dict({'a' : 1, 'b' : 2}, c=3) 
# print(a1) 
# print(a2) 
# print(a3) 
# print(a4)



# Дан словарь dict1, где ключами будут цены товаров, а значениями их названия, затем пройдитесь циклом по нему и поменяйте все ключи элементов, возведя их в квадрат, новые элементы запишите в словарь dict2

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}

# for k,v in dict1.items(): 
#     dict2.setdefault(k**2,v) 
# print(dict2)




# Из предыдущего словаря dict_, достаньте ключ, значение которого является максимальным, если значений несколько, распечатайте каждый из них по отдельности.

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

# mm = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k] == mm:
#         print(k)




# Дан словарь dict_, значениями, которого являются словари, измените словарь dict_ таким образом, чтобы значения внутреннего словаря стали внешними значениями

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
# print(dict_)


# Дан словарь dict1. Создайте словарь dict2, с ключами как в словаре dict1, а значениями пусть будут произведение чисел внутренних словарей

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}

# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): 
#         res = res * j 
#         dict2[k] = res 
# print(dict2)




# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}

# for i in int(list_):
#     if i.isalpha():
#         k = i
#         dict_.setdefault(k,v)
#     elif i%2:
#         v = i
#         dict_.setdefault(k,v)
    
# print(dict_)



# Дан список, состоящий из строк и чисел. Создайте словарь, ключами которого будут строки из списка, а значениями числа

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding'] 

# ls = [x for x in list_ if type(x)==int] 
# ls2 = [x for x in list_ if type(x)==str] 
# dict_ = dict(zip(ls2, ls)) 
# print(dict_)





# Дан словарь dict_. Отсортируйте словарь по значениям в порядке увеличения.
# Новые элементы занесите в словарь sorted_dict

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_dict = {k:item for item in sorted(dict_.values()) 
# for k,v in dict_.items()
#     if item == v} 
# print(sorted_dict)



# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {k:item 
# for item in sorted(dict_.values(), reverse=True) 
# for k,v in dict_.items() 
# if item == v} 
# print(sorted_dict)




# Дан словарь. Найдите сумму значений словаря, который хранится под ключом vars, используя значение словаря, под ключом math

# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }

# res = dict_.get('vars')

# for k,v in dict_.items():
#     for j in v.values():
#         if type(j) != int:

#             print(j(res.values()))





# a = {'a': 10, 'b': 9, 'c': 3}

# result = 1 

# for k, v in a.items():
    
#     result *= v
    
# print(result)



# нужно создать новый словарь, ключами которого будут буквы строки, а значениями числа, соответствующие количеству повторений данной буквы в строке.

# string = "pythonist" 

# dict_ = {}
# for i in string:
#     lenn = string.count(i)
#     dict_.setdefault(i,lenn)
# print(dict_)