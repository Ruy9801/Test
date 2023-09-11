# tuple 

# кортеж - неизменяемый тип данных, индексируемый, упорядоченный, итерируемый, предназначенный для зранения любых данных(в целом не отличаются от списков, просто их нельзяизменить и они занимают меньше памяти чем список)


# tuple_ = tuple()
# print(type(tuple_))

# tuple1 = (1,2,3)

# tuple2 = (1,2,3[1,2,3],{'a':1})
# tuple2[3].append(4)
# print(tuple2)


# tuple1 = 1,
# print(type(tuple1))

# tuple3 = tuple('hello')
# print(tuple3)


# ==========Методы tuple===========

# count - считает количество элементов

# tuple1 = (1,2,3,4,5,)
# print(tuple1.count(1))


# tuple1 = ('hello', 'hello', 'hello')
# print(tuple1.count('hello'))

# index - возвращает индекс первого вхождения

# tuple1 = (1,2,3,4,5,1)
# print(tuple1.index(3, 1))

# tuple1 = ([1,2,3], 1, 'h', [4,5,6], '1', 2, [7,8,9])

# tuple1[0].append(2)
# tuple1[3].append(2)
# tuple1[6].append(2)
# for rus in tuple1:
   
#     print(rus)

# for element in tuple1:
#     if type(element) ==list:
#         element.append(2)

# print(tuple1)