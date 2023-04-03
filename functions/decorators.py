"==============================Декоратор==============================="
# декоратор - функция высшего порядка, чтобы расширять функционал другой функции,
# не меняя ее

def decorator(func):
    def wrapper():
        print('функция вызывается')
        func()
        print('Функция заканчивается')
    return wrapper()

def func():
    print('hello')

res = decorator(func)
# res()

"========================Синтаксический сахар======================="
# def decorator(func):
#     def wrapper():
#         print('функция вызывается')
#         func()
#         print('Функция заканчивается')
#     return wrapper()

# @decorator
# def func():
#     print('hello')

# func()

from datetime import datetime

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = datetime.now()
#         res = func(*args,**kwargs)
#         end = datetime.now()
#         print(f"Функция отработала за {end-start}")
#         return res
#     return wrapper

from functools import cache

# @timer
@cache
def func(count):
    return(sum(range(count)))

print(func(10000000))

from datetime import datetime
def benchmark(func):
    def wrapper(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        end = datetime.now()
        print(f"Время выполнения: {end-start} секунд")
        return res
    return wrapper

@benchmark 
def fetch_webpage(): 
  import requests 
  webpage = requests.get('https://google.com')  

print(fetch_webpage())

