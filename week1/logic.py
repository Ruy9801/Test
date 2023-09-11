

# bool - булевый класс или тип данных

# a = True
# print(type(a))

# b = False
# print(type(b))


# print(int(True))
# print(int(False))


# # Здесь работает правило: все, что не 0 или не пустота, является правдой
# print(bool(3.4))
# print(bool(-150))
# print(bool(0))
# print(bool(' '))
# print(bool(''))



# ===================Присваивание и сравнение - разрые операции===================

# a = 10
# b = 5

# print(a + b > 14)
# print(a < 14 - b)
# print(a <= b + 5)
# print(a != b)
# print(a == b)
# c = a == b
# print(a, b, c,)




# x = 8
# y = 13 
# print(y < 15 and x > 8) # False  




# print(y < 15 or x > 8) # True  



# print(not y < 15) # False  




# a = 5 
# b = 0 
# print(not a) # False  
# print(not b) # True  


# цикл for позволяет пройтись по каждому элементу итерируемого объекта

# name = 'John'

# for letter in name:
#     print(letter)


# '''
# Синтаксис:

# name = 'john'

# for <var_name> in name:
#     pass

# '''

# # ================= Условные операторы

# money = 100

# if money > 100:
#     print('Покупаю 2л колу')  
# elif money == 0:
#     print('I will have to still')
# else:
#     print('Покупаю кефир')

# '''
# Синтакис:

# if < Условие1 >:
#     pass
# elif < Условие2 >:
#     pass
# else:
#     pass
# '''

# # if логическое_выражение: 
# #     выражение 1 
# #     выражение 2




# if n < 100: 
#     b = n + a 




# b = 0 
# a = 50 
# n = 98 
# if n < 100:
#     b = n + a 
# print(b) 




# # if логическое_выражение:
# #     выражение 1
# #     выражение 2
# # else:
# #     выражение 3 




# tovar1 = 50 
# tovar2 = 32 
# if tovar1 + tovar2 > 99: 
#     print("99$ недостаточно") 
# else: 
#     print("Чек оплачен") 




# a = 5 > 0 
# if a: 
#     print(a)
# if a > 0 and a < b: 
#     print(b - a) 




# user_is_logged_in = True 
# user_has_facebook_account = True 
# user_has_github_account = True 
# if user_is_logged_in: 
#     print("Logged in") 
# if user_has_facebook_account: 
#     print("Has FB account") 
# if user_has_github_account: 
#     print("Has Github account")




# user_is_logged_in = True 
# user_has_facebook_account = False 
# user_has_github_account = True 
# if user_is_logged_in: 
#     print("Logged in") 
# elif user_has_facebook_account: 
#     print("Has FB account") 
# elif user_has_github_account: 
#     print("Has Github account") 
# else: 
#     print("Not logged in and has no accounts")