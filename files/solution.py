# with open('task3.txt','w+') as file:
#     file.write("0*1*2*3*4*5*6*7*8*9* ")
#     file.seek(0)
#     print(file.read())
# task5
# res=[]
# with open('task5.txt','r') as file:
#     for (i) in file.readlines():
#         res.append(int(i))
# res.sort()
# with open('task6.txt','w+') as file:
#     print(f'{res[0]}-{res[-1]}')
#     file.write(f'{res[0]}-{res[-1]}')

# def read_last(lines: int, filename: str):
#     print(lines,filename)

# read_last('as',3)

#6
"""Напишите функцию read_last(lines: int, filename: str), которая будет
открывать определенный файл с именем filename и выводить в терминал строки, 
начиная с последней, в количестве lines. Обработайте ситуацию, 
в которой строк может быть больше, чем указано в lines(если их больше, 
просто выведите максимум строк
Для проверки вам дан файл «article.txt»."""

    
# def read_last(lines: int, filename: str):
#     with open(filename,'r') as file:
#         file_lines= file.readlines()
#         print(file_lines)
    
    

# read_last(3,'article.txt')

"""7"""
# def longest_words(filename:str):

#     with open(filename,'r') as file:
#         name = file.read()
#     list_ = name.split(" ")
#     print(max(list_,key=len))
# longest_words('article.txt')
# '''10'''
# def calc_price(filename:str):
#     res=[]
#     list_=[]
#     s=0
#     with open(filename,'r')as file:
#         res.extend(file.readlines())
#     for i in res:
#         list_.append(i.split(" "))

#     for i in list_:
#         s+=float(i[1])*float(i[2])
#     return s
       
# print(calc_price("prices.txt"))
"""2 решение"""
# import csv 
# def calc_price(filename: str) -> int: 
#     total_price = 0 
#     with open(filename, 'r') as file: 
#         reader = csv.reader(file, delimiter=' ') 
#         for row in reader: 
#             item_price = float(row[1]) * float(row[2]) 
#             total_price += item_price 
#     return float(total_price) 
# filename = 'prices.txt' 
# total_price = calc_price(filename) 
# print(f'Total price: {total_price} rubles')
"13"
# def bad_students(filename: str) -> list[str]:
#     with open(filename,'r') as file:
#         list_ = file.readlines()

#     my_list=[]
#     for s in list_:
#         s=s.strip()
#         if int(s[-1])<4:
#             splitted_text=s.split(' ')
#             my_list.append(splitted_text[1])
#     return my_list
# print(bad_students('zen_of_python.txt'))
"14"
# def reverse_file_print(filename: str)  :
#     with open(filename,'r') as filename:
#         list_ = filename.readlines()
#         for s in list_:
#             s=s[::-1]
#             print(s)

        

# reverse_file_print('zen_of_python.txt')
#1 JSON
# import json
# with open('task1.json','r') as file:
#     python_obj = json.loads(file.read())
# with open ('task1.py','w') as f:
#     f.write(str(python_obj))

#2
# import json
# with open('task2.json','r') as f:
#     json_obj = json.loads(f.read())
# python_obj = json_obj
# print(str(python_obj))

#3
import json
# json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]'
# python_products = json.loads(json_products)
# # print(python_products)
# for i in python_products:
#     if i["rating"]>4.0:
#         print(i['title'])
    
#7
# import json
# with open("db.json",'r') as file:
#     python_obj = json.loads(file.read())
# key,value = "description","..."
# for i in python_obj:
#     i.setdefault(key,value)

# with open('new_db.json','w') as file:
#     json.dump(python_obj,file)

#8
# import json
# with open("db.json",'r') as file:
#     python_obj = json.loads(file.read())

# for i in python_obj:
#     if i['id']==3:
#         python_obj.remove(i)
# print(python_obj)
# with open('new_db.json','w') as file:
#     json.dump(python_obj,file)

# 9
# import json 
# def create_new(id: int, title: str, description: str, price: int, rating:float) -> None: 
#     dict_={'id':id, 'title':title, 'description':description, 'price':price, 'rating':rating} 
#     with open('db.json') as file: 
#         res = json.load(file)
#         res.append(dict_) 
#     with open('new_db.json', 'w') as f: 
#         f.write(json.dumps(res)) 
# create_new(10, 'assa', 'asd', 12, 25.0)

#10
# import json
# def get_sorted(json_filename: str) -> list[dict]:
#     with open(json_filename) as file:
#         f = json.load(file)
    
#     f.sort(key=lambda x:x['rating'],reverse=True) 
#     return f 
# print(get_sorted('db.json'))

"11"
# def update(id: int, title: str, price: int, rating: float) -> None:
#     dict_={id,title,str,price,rating}
#     with open('new_db.json') as file:
#         db = json.load(file)
# #     for i in db:
# #         if id not in i['id']:
# #             raise ValueError
# #         # else:
# update(1,'qwe',111,4.9)
# def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
#     with open('new_db.json', 'r') as f:
#         db = json.load(f)
#     for product in db['products']:
#         if product['id'] == id:
#             if title is not None:
#                 product['title'] = title
#             if price is not None:
#                 product['price'] = price
#             if rating is not None:
#                 product['rating'] = rating
#             with open('new_db.json', 'w') as f:
#                 json.dump(db, f)
#             # return
#     raise ValueError(f"No product with ID {id}")
# update(id=1234, price=999, rating=4.5)
import json
# def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
#     with open('db.json', 'r') as f:
#         db = json.load(f)
#     for product in db:
#         if product['id'] == id:
#             if title is not None:
#                 product['title'] = title
#             if price is not None:
#                 product['price'] = price
#             if rating is not None:
#                 product['rating'] = rating
#             with open('db.json', 'w') as f:
#                 json.dump(db, f)
#             return
#     raise ValueError(f"No product with ID {id}")
# update(id=5678, title="New Title")

        

        
#12
# import json
# def search(name: str) -> list[dict]:
#     with open('db.json') as f:
#         db = json.load(f)
#         print(db)
#     res = list(filter(lambda n:name in n['title'],db ))
#     return res
# print(search('sam'))

#13
# import json
# def filter_by_price(price: int) -> list[dict]:
#     with open('db.json') as f:
#         db = json.load(f)
#     res = list(filter(lambda x:x['price']>=price,db))
#     return res
# print(filter_by_price(1000))

"14"



# def bulk_create(products: list[dict]) -> None:
#     with open('db.json', 'r') as f:
#         db_data = json.load(f)

#     # Create a set of existing product IDs in new_db.json
#     existing_ids = set(product['id'] for product in db_data)

#     for product in products:
#         if product['id'] not in existing_ids:
#             db_data.append(product)
#             existing_ids.add(product['id'])


#     with open('new_db.json', 'w') as f:
#         json.dump(db_data, f)

# print(bulk_create([{"id": 11, "title": "assa", "description": "asd", "price": 12, "rating": 25.0}]))
                

res=['asd','qwerty','asdasdasdasd','dsa']
answer = list(
    filter(lambda x: len(x)>3,
           map(lambda x:x.title(),res)))
print(answer)
