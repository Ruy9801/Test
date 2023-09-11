
# lambda - анонимная функция(та же самаая функция но без названия)

# lambda параметр : что функция возвращает 

# def add_nums(a,b):
#     return a + b

# print(add_nums(2,3))



# result = lambda a,b : a + b

# print(result(2,3))



# x = lambda a,b,c: (a*b)%c

# print(x(1,6,3))


# dict1 = {1: 5, 3: 5, 6: 2}
# get_keys = lambda x : x.keys()
# print(get_keys(dict1))



# square = lambda a: a ** 2
# print(square(5))


# list1 = [1,2,5,6]
# get_last = lambda ls: ls[-1]
# print(get_last(list1))



# ==================================

# map(function, iterable) - функция которая принимает функцию и итерируемый обьект
# она применяет функцию к каждому элементу в iterables



# map_get = map(int,['1','2','3','4'])
# print(list(map_get))



# nums = [1,2,3,4,5,6]

# def square(num):
#     return num * num

# map_func = map(square, nums)

# print(list(map_func))




# list1 = [1, -8, 22, 98, -88]

# list2 = list(map(lambda x: x>0, list1))

# print(list2)



# func = lambda e: e+1
# res = []
# for e in [1,2,3,4,5,6]:
#     res.append(func(e))

# print(res)



# filter(function, iterable)  - функция принимает первым аргументом другую функцию и итерируемый обьект 
# результато будет последовательность котрые прошли условия filter



# nums = [1,2,3,4,5,6,7,8,9,10]

# res = list(filter(lambda e: e%2==0, nums))

# print(res)



# list1 = ['Ryu', 'Kevin', 'Marko', 'Stiv', 'Raya', 'Ryukaku']

# res = list(filter(lambda i: i[0]=='R', list1))

# print(res)




# list1 = ['Ryu', 'Kevin', 'Marko', 'Stiv', 'Raya', 'Ryukaku']

# def sort1(name):
#     values = 'KRHTHALS'
#     # print(tuple(values))
#     return name.upper().startswith(tuple(values))

# print(sort1('Ryu'))

# res = []

# for name in list1:
#     if sort1(name):
#         res.append(name)

# print(res)


# res2 = list(filter(sort1, list1))
# print(res)




# reduce  -  эта функция принимает функцию и возвращает 1 результат
# (ее убрали из стандартной библиотеки питона так как ей нашли замену sum max)


# from functools import reduce


# lst = [1,2,3,4,5]


# result = reduce(lambda x,y: x+y, lst)
# print(result)



# lst = [1,2,3,4,5,6,7,8]

# def mul(a,b):
#     return a*b

# res = reduce(mul, lst)
# print(res)



# enumerate(iterable, ['start - c какого начинать элемента по дефолту 0'])  -   функция принимает последовательность возвращает tuple состаящий из числа и элемента 


# lst = ['a','bb', 'ccc', 'dddd']

# for i in enumerate(lst[1]):
#     print(i)


# for i in enumerate(lst[1:]):##                 ===================================================== SUPER USFULL 11111111111111
#     print(i) 


# for i in enumerate(lst, 10):
#     print(i)




# lst = ['Ryu','Kage','Fuorandy']

# res = list(enumerate(lst,1))
# print(res)





# zip(iterable, iterable .....) - сопоставляет каждый элемент из intrable со следующим 


# list1 = [1,2,3,4,5,6]
# list2 = ['a','b','c','f','d', 'v']
# list3 = [6,9,0,7,9,8]

# print(list(zip(list1, list2, list3)))
# print(dict(zip(list1,list2)))




# any(iterable) - возвращает True если хотя бы один элемент в iterible имеет значение True


# lst = [1,2,3,4,5]
# lst1 = [0, False]
# res = any(lst)
# res1 = any(lst1)
# print(res)
# print(res1)



# all(iterable) возвращает True если все элементы является True 

# lst = [True,False,True,True]
# print(all(lst))



# '''изменить тип данных значений'''
# dict_ = {1: 2, 3: 4, 5: 6}


# res = list(map(lambda k : str(k), dict_ ))

# print(res)


# """задача при помощи map() заменить значение чисел словами четное.нечетное"""
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = list(map(lambda v:  'четное'  if v%2==0 else 'нечетное', lst))

# print(res)





# =========================Tusks 


# lst = [25,'sdf', 2,33, 1, True]
# part = list(filter(lambda c: type(c) == int, lst))
# res = list(map(lambda v: v**0.5, part))

# print(res)



# from functools import reduce

# lst = ['R','y','u','D','a','k','y']

# # res = reduce(lambda v,s: v+s, lst )

# # print(res)



# lst.remove()

# print(lst)





# =============================Tasks planform







