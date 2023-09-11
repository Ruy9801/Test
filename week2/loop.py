# циклы - это блок кода, который повторяется определенное количество раз или работает беспонечно

# for - цикл, который работает  с итерируемыми обьектами и закончит свою работу на последнем элементе

# while - циел, который работает пока условие будет верно

# while True - пока Правда
# после while  идет условие цикла и пока это условие верно, то цикл будет работать

# остановить цикл можно комбинациями ctrl + c или ctrl + z

# while True:
#     print('Hello world')


# counter = 0
# while True:
#     counter += 1
#     print(counter)



# count = 0
# while count != 101:  # --- пока count не равен 101
#     print(count)
#     count += 1
# print('end')



# count = 10
# while count != 0:
#     print(count)
#     count -= 1
#     count = count - 1
# print('end')



# a = 0 
# while a:
#     print('hello') # --- не отработает потому что условие False



# for i in range(1,10):
#     print(i + 1)

# list1 = list(range(1,10))
# print(list1)



# for i in 12345: # --- int' object is not iterable
#     print(i)
# тип данных int не итерируемый обьект



# num = 123345678
# sum = 0 

# for i in str(num):
#     sum += int(i)

# print(sum)



# string = 'hello'
# string1 = 'world'
# for i in range(len(string)):
#     print(i, string[i], string1[i])

# 0 h w
# 1 e o 
# 2 l r  ---- работает только с переменными одинаковой длинны
# 3 l l 
# 4 o d 



# list_ = [1,2,3]  
# for i in list_:    # ---- бесконечный цикл с помощью for
#     print(i)
#     list_.append('hello')
#     print(list_)
#     if len(list_) == 100:
#         break



# ========== ключевые слова в циклах ===========


# break = полностью выйти из цикла досрочно прерывает цикл

# continue = перейти к следующей операции ----------------------usfull




# for i in range(10):
#     if i == 3:
#         continue
#     print(i)



# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
#     print(i)



# for i in range(10):
#     print(i)
#     if i == 3: 
#         break
#     print(i)



# i = 0
# while i < 6:
#     if i == 3: 
#         break
  
#     print(i)
#     i += 1



# for i in range(10):
#     if i < 3: continue
#     print(i)



# for i in range(10):
#     print(i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             break
#     if i == 2:
#         break



# list_ = [2, 1, 3, 6, 2, 5, 2, 8, 2]

# while 2 in list_:
#     list_.remove(2)
# print(list_)



# while True:
#     print(1)
#     continue
#     print(2)
    


# else примененное в цикле for и while, проверяет, был ли произведен выход из цикла с помощью  break, или же естественным образом
# else работает если выход из цикла был совершен без помощи break 

# for i in 'hello world':
#     if i =='d':
#         break
# else:
#     print('hello world')   # Ничего не выйдет



# for num in range(5):
#     if num < 3:
#         pass           # pass -- функция чтобы не было синтастической ошибки pass = пустота, балванга, пуголо
#     else:
#         print(num)



# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# for key in dict1:
#     print(key)


# for value in dict1:
#     print(dict1[key])



# for items in dict1.items():
#     print(items)



# items = (1,2)
# key,value = items
# print(key,value)


# for items in dict1.items():
#     key = items[0]
#     value = items[1]
#     print(key, value)


# for a,b,c in [(1,2,3), (4,5,6), (7,8,9)]:
#     print(a,b,c)


# operator = input("enter operator + - / *: ")
# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))


# while True:
#     if operator == "+":
#         print(num1 + num2)
  
#     elif operator == "-":
#         print(num1 - num2)

#     elif operator == "*":
#         print(num1 * num2)

#     elif operator == "/":
#         print(num1 / num2)

#     gett = input('Хотите продолжить? Ответ Да или Нет: ')


#     if gett.lower() == 'yes':
#         pass
#     elif gett.lower() == 'no':
#         break
#         print('Вы закончили работу!')
#     else:
#         print('Type Yes or No')
        


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = []
# for key in my_dict:
#     keys.


# =====================Tasks


# while True:
#     password = input("password: ")

#     if len(password) < 8:
#         print("Пароль должен содержать минимум 8 символов")
#         continue
#     elif password.islower() == True:
#         print("Пароль должен содежать хотя бы одну заглавную букву")
#         continue
#     elif password.isupper() == True:
#         print("Пароль должен содержать хотя бы одну строчную букву")
#         continue
#     elif password.isalpha() == True:
#         print("Пароль должен содержать хотя бы одну цифры")
#         continue
#     elif password.isalnum() == True:
#         print("Пароль должен содержать хотя бы специальный символ (например, !, @, #, $ и т.д.")
#         continue
#     else:
#         print(password)
#         break




# name_of_list = ['RyuDzaky']
# nelist = str(name_of_list)
# new_list = list(nelist[2:-2])
# num = int(len(new_list ) / 2)

# if int(len(new_list ))%2 != 0:
#     print(new_list [(num + 1):] + new_list [:(num + 1)])
# else:
#     print(new_list [num:] + new_list [:num])


# string = ['RyuDzakyA']
# strin = string[0]
# center = len(strin) // 2

# piss1 = strin[center:] + strin[0:center]
# piss2 = strin[center+1:] + strin[:center+1]

# if len(strin)%2==0:
#     print(piss1)
# elif len(strin)%2!=0:
#     print(piss2)
