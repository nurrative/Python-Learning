"=====================================Функции======================================"
# Функция - это именнованный блок кода, который принимает аргументы и возвращает
# результат

func = lambda num1,num2: num1+num2
res =func(5,10)
print(res) #15
# lambda - ключевое слово, для создания анонимной функции

def my_sum(num1,num2):
    return num1+num2

res=my_sum(12,45)
print(res)

def calc(num1,num2, oper):
    """
    oper - строка, с операцией для вычислений
    "+" - cложение
    "-" - вычитание
    """
    if oper =="+":
        return num1+num2
    if oper=="-":
        return num1-num2
    if oper=="*":
        return num1*num2
    if oper=="/":
        return num1/num2            

print(calc(10,12,"+")) #22
print(calc(20,8,"-"))  #12
print(calc(10,2,"*"))  #20
print(calc(15,5,"/"))  #3
print(calc(15,5,"6")) #None

def my_len(obj):
    "Возвращает длину обьекта"
    count = 0
    for i in obj:
        count += 1
    return count

print(my_len([15,23,64,23,12])) #5
print(my_len("asdsadasdasd")) #12
print(my_len({'a':1,'b':2})) #2

def super_len(obj):
    try:
        #если мы можем итерировать обьект
        return my_len(obj)
    except:
        #если не можем, то будем итерировать в виде строки
        return my_len(str(obj))   

print(super_len([1,2,3,4])) #4
print(super_len(123456789)) #9
print(super_len(None)) #4

"===================================DRY============================"
#DRY - don't repeat yourself (не повторяйся)


"=============================Аргументы и параметры==================="
# параметры - это локальные переменные, значения которым мы задаем 
# при вызове функции
# аргументы - значения, которые мы задаем параметрам при вызове функции

def func():
    local_var = 5

"=========================Виды аргументов и параметров================"
# Параметры бывают 2 видов:
# 1. Обязательные
# 2. Необязательные
# 2.1 c дефолтными значением(по умолчанию) 
# 2.2 args (arguments)
# 2.3 kwargs (key word arguments)

def func(a,b='default',*args,**kwargs):
    print(a,b,args,kwargs)

# func()   TypeError: func() missing 1 required positional argument: 'a'
func('hello') #hello default
func('hello',100) #hello 100
func('hello',100,34,21,"world") #hello 100 (34, 21, 'world')
func('hello',100,34,21,"world",key1='value',key2='500') 
#hello 100 (34, 21, 'world') {'key1': 'value', 'key2': '500'}
# func('hello',a=200) TypeError: func() got multiple values for argument 'a'


"=====================Виды аргументов========================"
# позиционные (по порядку параметра)
# именнованные(по имени параметра)

def func2(a,b):
    print(f"a = {a}, b = {b}")


func2(10,20)        #a = 10, b = 20 - позиционно
func2(a=30,b=40)    #a = 30, b = 40 - именновано
func2(b=50,a=60)    #a = 60, b = 50 - именновано


"========================Звездочки==========================="
list1=[1,2,3,4]
list2=[4,5,6,*list1]
print(list2) #[4,5,6,1,2,3,4]
dict1 = {'key1':1, 'key2': 2}
list3 = [*dict1]
print(list3) #['key1', 'key2']
dict2 = {'a':3,'b':4}
dict3 ={**dict2,**dict1}
print(dict3) #{'a': 3, 'b': 4, 'key1': 1, 'key2': 2}

dict_={'a':1,'b':2,"c":3}

def dictionary(dict_):
    list_=[]
    for i in dict_:
        list_.append(i)
    return (list_)
print(dictionary(dict_))

def is_palindrome(name):
    if name==name[-1]:
        return True
    else: return False

print(is_palindrome('довод'))
