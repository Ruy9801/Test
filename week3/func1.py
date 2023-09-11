


# CRUD

# Create
# Read
# Update
# Delete

# import datetime

# data = [
#     {
#         'id': 1,
#         'name': 'iphon 14',
#         'price': 80000,
#         'created_at': datetime.datetime(2022, 9, 4),
#         'is_active': True
#     },
#     {
#         'id': 2,
#         'name': 'Manga Solo Leveling',
#         'price': 200,
#         'created_at': datetime.datetime(2020, 7, 3),
#         'is_active': True
#     },
#     {
#         'id': 3,
#         'name': 'Anime Blich',
#         'price': 400,
#         'created_at': datetime.datetime(2010, 6, 2),
#         'is_active': False
#     }
# ]


# def get_all():
#     return data

# # print(get_all())



# def get_one(id):
#     for i in data:
#         if i['id'] == id:
#             print(i)

# # get_one(2)




# def post_product():
#     max_id = max([i['id'] for i in data])
#     new_data = {
#         'id': max_id + 1,
#         'name': input('Имя: '),
#         'price': int(input('Цена: ')),
#         'created_at': datetime.datetime.now(),
#         'is_active': True
#     }
#     data.append(new_data)
#     return '201 CREATED', new_data

# # print(post_product())




# def patch_product(id):
#     product = [i for i in data if i['id'] == id]
#     index = data.index(product[0])
#     if product:
#         data.remove(product[0])
#         name = input('Имя: ')
#         price = int(input('Цена: '))
#         product[0]['name'] = name
#         product[0]['price'] = price
#         product[0]['created_at'] = datetime.datetime.now()
#         product[0]['is_active'] = True
#         data.insert(index, product[0])
        
#         return 'Успешно изменено'
#     else:
#         return '404', 'Вы ввели неправильные данные'

# # print(patch_product(3))





# def del_product(id):
#     product = [i for i in data if i['id'] == id]
#     if product:
#         data.remove(product[0])
#         return  'Deleted'
#     else:
#         return 'Has no find'

# # print(del_product(3))




# def main():
#     print('Hello, you have next fanctions:\n\tPOST\n\tGET\n\tDETAIL\n\tPUT\n\tDELETE')
#     method = input('Введите одну из функции: ').upper()

#     if method == 'GET':
#         print(get_all())

#     elif method == 'DETAIL':
#         id = int(input('Введите id: '))
#         print(get_one(id))

#     elif method == 'POST':
#         print(post_product())

#     elif method == 'PUT':
#         id = int(input('Введите id: '))
#         print(patch_product(id))

#     elif method == 'DELETE':
#         id = int(input('Введите id: '))
#         print(del_product(id))

# main()



# ==========================Tasks===========================


# import datetime

# data = [
#     {
#         'id': 1,
#         'category': 'Веб-разработка',
#         'sub_category': 'Python',
#         'header': "WebDev Mastery: Build & Create",
#         'description': "Наш курс по веб-разработке поможет вам освоить современные технологии и навыки для создания впечатляющих веб-сайтов и приложений.",
#         'level': 'начальный',
#         'price': 65000
        

#     },
#     {
#         'id': 2,
#         'category': 'Разработка мобильных приложений',
#         'sub_category': 'JavaScript',
#         'header': "Mobile App Development: Create, Code, Launch",
#         'description': "Научитесь создавать мобильные приложения от идеи до релиза вместе с нашим курсом разработки мобильных приложений.",
#         'level': 'средний',
#         'price': 75000

#     },
#     {
#         'id': 3,
#         'category': 'Разработка игр',
#         'sub_category': 'Java',
#         'header': "Game Development: Create, Code, Play",
#         'description': "Изучите искусство создания захватывающих игр с нашим курсом разработки игр.",
#         'level': 'профессиональный',
#         'price': 90000

#     }
# ]



# def get_all():
#     return data




# def get_one(id):
#     for i in data:
#         if i['id'] == id:
#             print(i)





# def create():
#     max_id = max([i['id'] for i in data])
#     count = 0


#     while count == 0:
#         category = input('Введите категорию (Веб-разработка, Разработка мобильных приложений, Разработка игр): ')
#         if category == 'Веб-разработка' or category == 'Разработка мобильных приложений' or category == 'Разработка игр':
#             count += 1
#             category1 = category

#     while count == 1:
#         sub_category = input('Введите подкатегирий (Python, JavaScript, Java): ')
#         if sub_category == 'Python' or sub_category == 'JavaScript' or sub_category == 'Java':
#             count+=1
#             sub_category1 = sub_category

#     while count == 2:
#         header = input('Введите заголовок курса (максимум 60 символов): ')
#         if len(header.split()) <=60:
#             count += 1
#             header1 = header

#     while count == 3:
#         description = input('Введите описание курса (минимум 10 слов): ')
#         if len(description) >= 10:
#             count += 1
#             description1 = description

#     while count == 4:
#         level = input('Введите уровень курса (начальный, средний, профессиональный): ')
#         if level == 'начальный' or level == 'средний' or level == 'профессиональный':
#             count += 1
#             level1 = level

#     while count == 5:
#         price = int(input('Цена в сомах Например: 80000: '))
#         if type(price) == int:
#             count += 1
#             price1 = price

#     new_data = {
#     'id': max_id + 1,
#     'category': category1,
#     'sub_category': sub_category1,
#     'header': header1,
#     'description': description1,
#     'level': level1,
#     'price': price1

#     }

#     data.append(new_data)
#     return '201 CREATED', new_data





# def update(id):
#     product = [i for i in data if i['id'] == id]
#     index = data.index(product[0])
#     if product:
#         data.remove(product[0])
#         count = 0
#         while count == 0:
#             category = input('Введите категорию (Веб-разработка, Разработка мобильных приложений, Разработка игр): ')
#             if category == 'Веб-разработка' or category == 'Разработка мобильных приложений' or category == 'Разработка игр':
#                 count += 1
#                 category1 = category

#         while count == 1:
#             sub_category = input('Введите подкатегирий (Python, JavaScript, Java): ')
#             if sub_category == 'Python' or sub_category == 'JavaScript' or sub_category == 'Java':
#                 count+=1
#                 sub_category1 = sub_category

#         while count == 2:
#             header = input('Введите заголовок курса (максимум 60 символов): ')
#             if len(header.split()) <=60:
#                 count += 1
#                 header1 = header

#         while count == 3:
#             description = input('Введите описание курса (минимум 10 слов): ')
#             if len(description) >= 10:
#                 count += 1
#                 description1 = description

#         while count == 4:
#             level = input('Введите уровень курса (начальный, средний, профессиональный): ')
#             if level == 'начальный' or level == 'средний' or level == 'профессиональный':
#                 count += 1
#                 level1 = level

#         while count == 5:
#             price = int(input('Цена в сомах Например: 80000: '))
#             if type(price) == int:
#                 count += 1
#                 price1 = price


#         product[0]['category'] = category1
#         product[0]['sub_category'] = sub_category1
#         product[0]['header'] = header1
#         product[0]['description'] = description1
#         product[0]['level'] = level1
#         product[0]['price'] = price1
#         data.insert(index, product[0])
        
#         return 'Успешно изменено'
#     else:
#         return '404', 'Вы ввели неправильные данные'





# def delete(id):
#     product = [i for i in data if i['id'] == id]
#     if product:
#         data.remove(product[0])
#         return  'Deleted'
#     else:
#         return 'Has no find'
    


    
# while True:

#     def main():
#         print('Привет, вам доступны следующие функции:\n\tPOST\n\tGET\n\tDETAIL\n\tPUT\n\tDELETE')
#         method = input('Введите одну из функции: ').upper()

#         if method == 'GET':
#             print(get_all())

#         elif method == 'DETAIL':
#             id = int(input('Введите id: '))
#             print(get_one(id))

#         elif method == 'POST':
#             print(create())


#         elif method == 'PUT':
#             id = int(input('Введите id: '))
#             print(update(id))

#         elif method == 'DELETE':
#             id = int(input('Введите id: '))
#             print(delete(id))


#     main()


    





# database = [
#     {
#      'title': 'str',
#      'price': 33, 
#      'category': 'str'
#      }
# ]

# def create(database,title,price,category):
#     dict1 = {
#         'title': title,
#         'price': price,
#         'category': category
#     }
#     return database.append(dict1)

# create(database, 'anim',233,'anime')

# def read(database):
#     return database

# print(read(database))


# def update(database,index,title,price,category):

    
#     database[index]['title'] = title
#     database[index]['price'] = price
#     database[index]['category'] = category
#     return database


# print(update(database,1,'toto',233,'cara'))


# def delete(database, index):
#     del database[index]
#     return database

# print(delete(database, 1))
