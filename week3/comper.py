# comprehension - генерация последовательностей в одну строку используя цикл
# также его называют синтаксическим сахарам


# index = 0

# for i in range(1,10):
#     index += 1

#     index = index + 1



# основной целью использования как list, dict comprehension является упрощение и повышение читаемости кода

# list comprehension - это упрощенный подход к созданию списка который задействует цикл for а также мы можем использовать if else операторы под капотам генератор списков также использует цикл for но по скорости он быстрее потому что не использует метод append()



# list_ = []
# for i in range(1,11):
#     list_.append(i**2)

# print(list_)


# list_ = (i**2 for i in range(1,11))    # результат for элумент in итерируемый обект
# print(list(list_))



# import time

# start_time = time.time()
# list1 = []

# for i in range(100):
#     list1.append(i)

# time1 = time.time() - start_time

# print(time1)


# start_time1 = time.time()  
# list2 = [i for i in range(100)] 
# time2 = time.time() - start_time1
# print(time2)


# list_ = [i for i in range(1,11) if not i%2]
# print(list_)


# list_ = [i for i in range(0,11,2)]
# print(list_)



# list_ = ['hello' for i in range(10)]
# print(list_)



# print([input() for i in range(10)])



# если в условии нужен else, то все условие пишется до for 

# list_ = ['нечетное' if i % 2 else 'четное' for i in range(1,11)]
# print(list_)



# list1 = [1,'hello', 2, 'a', 4.0, '7', 8]

# a = ['нечетное'  if i%2 else 'четное' for i in list1 if type(i) == int or type(i) == float]

# print(a)



# set comrehesion - разница с list comprehesion что выходные данные не содержит дубликатов 


# list_ = [1,2,3,4,5,1,5,5,2]

# set_ = {i for i in list_}

# print(set_)


# list_ = [1,2,3,4,5,1,5,5,2]

# set_ = set()
# for i in list_:
#     set_.add(i)
# print(set_)



# dict comprehesion - аналогично создаются, но обязательно нужно указывать key: value 

# squaeres = {i: i **i for i in range(10)}
# print(squaeres)



# squ = {}

# for k in range(10):
#     squ.setdefault(k,k**k)
#     squ.update({k: k**k})
# print(squ)



# list_ = [1,2,3,4,5,6,7,8]

# dict_ = {i: list_.count(i) for i in list_}

# print(dict_)



# d = {'a': 2, 'c':3}

# dict_ = {k: 'четное' if v %2==0 else 'нечетное' for k,v in d.items()}

# print(dict_)




# dict1 = {k: str(k) for k in range(1,11) }

# print(dict1)



# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# dict_ = {list1[index]:list2[index] for index in range(len(list1))}
# print(dict_)




# dict1 = {'a': 1, 'b':2, 'c':3}

# dict2 = {k: v for k,v in dict1.items()}

# print(dict2)



# dict1 = {'a': 1, 'b':2, 'c':3}

# dict2 = {v:k for k,v in dict1.items()}
# print(dict2)



# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }



# dict2 = {k:sum(v) for k,v in dict1.items()}

# print(dict2)



# list1 = [['hello world' for i in range(5)] for i in range(10)]

# print(list1)



# num = input('Введите число:')
# res = []
# for nums in num:
#     res.append(int(nums))

# print(sum(res))


# new_dict = {k:i for k,v in dict_.items() for i,j in v.items() if j == max(v.values())} 
# print(new_dict)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:v for k,l in my_dict.items() for c,v in l.items()} 

# print(dict_)



# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# res = [[k[0],k[1]*42] for k in prairie_pirates if k[2]==True]

# print(res)



# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# res = [v['likes'] for v in dict_.values() if v['rating'] > 3 ]

# print(sum(res))



# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# dict1 = [c['id'] for a,b in dict_.items() for c in b['comments'] if len(dict_[a]['comments'])>3]

# print(dict1)


# list_ = [i/2 for i in range(0,11) if i%2==0]

# print(list_)


# set1 = {x for x in range(10)} 
# set2 = {a for a in range(8,18)}

# full_set = set1.union(set2)

# if len(full_set)<20:
#     print(f'В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set)==20:
#     print('Ваш объединенный сет полностью уникальный!')



# word = 'lol'
# word1 = 'lol'

# if word == word1:
#     print('dd')