# def multiply_list(list_):
#     n=1
#     for i in list_:
#         n=n*i
#         print(n)
#     return n    

# print(multiply_list([1, 2, 3, 4, 5, 6]))

# def  sum_digits(num):
#     sum=0
#     for i in str(num):
#         sum=sum+int(i)
#     return sum

# print(sum_digits(105))

# def func12(my1,case):
#     l1=[]
#     if case=="lower":
#         for i in my1:
#             l1.append(i.lower())
#         return l1
#     else:
#         for i in my1:
#             l1.append(i.upper())
#         return l1
    
# print(func12(["hEllo", "wORld"], "lower"))

# def func13(string):
#     dict_={}
#     for i in string:
#         dict_[i]=string.count(i)
#     return dict_
# print(func13("Hello"))

# a = {'x': 1, 'y': 2, 'z': 1}
# print(a.get('x'))

# a = {'a': 1, 'b': 2, 'c': 3}
# b={}
# for k,v in a.items():
#     b[v]=k
# print(b)


# words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# # short_words = list(filter(lambda x: len(x) >= 5, words))
# # upper_short_words = list(map(lambda x: x.upper(), short_words))


# short_upper_words = list(map(lambda x: x.upper(), filter(lambda x: len(x) >= 5, words)))
# print(short_upper_words)


# # short_upper_words = []
# # for word in words:
# #     if len(word) >= 5:
# #         short_upper_word = word.upper()
# #         short_upper_words.append(short_upper_word)

# # tuple_=()

# # def func(num):
# #     if num==7:
# #         return func(num)
   
    
# x = "Я глобальная переменная!"

# def my_func():
#     global x
#     x='Я могу изменяться'

# print(my_func())

# num = 3
# def mul():
#     global num
#     num = pow(num,2)
# mul()
# mul()
# mul()
# print(num)

# result = 0
# def pow_first(x,y):
#     global result
#     result=x**y
# def pow_second(z):
#     global result
#     result=result%z

# pow_first(2, 3)
# pow_second(3)
# print(result)

# from functools import reduce
# list_ = [1, 2, 3, 4] 
# result = reduce(lambda x,y: x*y,list_)
# print(result)

# a = ['pipi', 'papa', 'mama']
# b=[]
# def upper():
#     for i in a:
#         b.append(i.capitalize())
# upper()
# print(b)
#4
# balance = 0

# def get_salary(amount):
#     global balance
#     balance=balance+amount
    
# def pay_bills(amount, log_name):
#     global balance
#     balance = balance-amount
    
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
    
#     print(f'У вас на счету: {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control():
#     global a
#     for k,v in a.items():
#         if v>=17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control')

# age_control()



# def count_symbols(string):
#     vowels = set("аеиоуыэюя")
#     consonant = set("йцкнгшщзхъфвпрлджчсмтб")
#     vowels_count = 0
#     consonant_count = 0
#     symbols_count = 0
#     for char in string:
#         if char.lower() in vowels:
#             vowels_count += 1
#         elif char.lower() in consonant:
#             consonant_count += 1
#         else:
#             symbols_count += 1
#     return (f"Количество гласных: {vowels_count}, согласных: {consonant_count}, остальных символов: {symbols_count}")
# print(count_symbols('Мурат супер!'))

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def lower_7():
#     b=list(i for i in a if i<7)
    
#     return b
    
# print(lower_7())  

# def foo():
#     global var
#     var = 'переменная foo'
  
#     def bar():
#         global var
#         print('переменная в foo: ', var)
#         var = 'переменная bar'

        
        
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# def calc(x,y,z):
#     if z=="+":
#         return add_(x,y)
#     elif z=="-":
#         return sub_(x,y)
#     elif z=="*":
#         return mult_(x,y)
#     else: 
#         return div_

# def add_(a,b):
#     return a+b

# def sub_(a,b):
#     return a+b
    
# def mult_(a,b):
#     return a+b
    
# def div(a,b):
#     return a+b

# print(calc(2,5,'+'))
#15
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' }, 
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users):
#     string=""
#     for i in users:
#         if i['work'].startswith("IT"):
#             string+=(f"{i['name']}, скидки в магазине компьютерной техники!\n")
#     return string

# print(func15(users))

#17
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# def func17(employ):
#     for i in employ:
#         i['salary']=i['salary']+200*i['overTime']
#         i.pop('overTime')
#     return employ
            

# func17(employees)

#18
# def func18(lst):
#     str_list=[]
#     int_list=[]
#     for i in lst:
#         if type(i)==str:
#             str_list.append(i)
#         elif type(i)==int:
#             int_list.append(i)
#     return int_list, str_list

# print(func18([1,2,3,4,'a','b']))

#19
students = [ 
{'student': 'Jack', 'marks': 43}, 
{'student': 'Tom', 'marks': 92}, 
{'student': 'Helen', 'marks': 85}, 
{'student': 'Peter', 'marks': 58}, 
{'student': 'Jessica', 'marks': 78} ] 

def func19(list_): 
    list_.sort(key=lambda x:x['marks'],reverse=True) 
    return list_ 
print(func19(students))

#20
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]
# res=[]
# def func20(list_,string):
#     for s in list_:
#         if string.lower() in s['title']:
#             res.append(s)
#     return res
# func20(products,'i')

# 21
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func21(list_,string):
#     res=[]
#     for s in list_:
#         if string.lower() == s['category'].lower():
#             res.append(s)
#     return res
# print(func21(products,'samsung'))

# database=[]
# def create(db:list,title:str,price:int,category:str):
#     database.append({title:'str',price:'123',category:'my_category'})
#     return db
# create()

# from functools import reduce
# list_ = [5, 6, 7, 8]
# result = reduce(lambda x,y:x*y,list_)
# print(result)

# list_ = [-1, 2, 3, 5, -3, 7]
# result= list(map(lambda x:x>0,list_))
# print(result)


# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x,y:x if len(x)>len(y) else y,list_)
# print(result)

# #12
# from functools import reduce 
# list_ = [1,2,3,4,5,6,7] 
# result = reduce(lambda x,y: max(x,y), list_) 
# print(result)

# #13
# from functools import reduce 
# list_ = [1,2,3,4,5,6,7] 
# result = reduce(lambda x,y: min(x,y), list_) 
# print(result)
