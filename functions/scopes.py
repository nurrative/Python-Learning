"========================Области видимости/ пространства имен======================"
#LEGB - (local,enclosed, global,build-in)

#build-in - встроенное пространство : input, int, str, sum

#глобальное пространство (наш файл) - globals 

#enclosed - замкнутое пространство(находится между двумя пространствами)
#локальное пространство, внутри которого есть еще одно постранство


var = 'глобальная'

def func():
    var='замкнутая'
    print(var)
    def inner():
        var = 'локальное'
        print(var)
    inner()
func()
print(var)

#local - локальное пространство(внутри функции)

a = 'hello'

def func(a,b):
    print("GLOBALS", globals())
    print("LOCALS", locals())

func(10,50)

# num1 = 10
# def func():
#     print(num1)
# func()

# counter=0

# def increase_counter():
#     global counter
#     counter+=1
#     print(counter)
# increase_counter() #1
# increase_counter() #2
# increase_counter() #3
# increase_counter() #4

# def count(i):
#     counter=0

#     def increase_counter():
#         nonlocal counter
#         counter+=1
#         print(counter)
#     for _ in range(i):
#         increase_counter()

# count(10)

def func():
    a=10
    def inner_func():
        a=15
        def inner_inner_func():
            nonlocal a
            a+=1
        inner_inner_func()
        print(a)
    inner_func()
func()

    
