"==========================Встроенные функции=========================="
#enumerate

string = 'Hello'
enum = enumerate(string)
print(enum) #<enumerate object at 0x10064d260>
print(list(enum)) #[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

string = 'World'
enum = enumerate(string,5)
print(list(enum)) #[(5, 'W'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]

#дан список с числами, умножьте на 2 все числа под нечетным индексом, умножьте 
# на 3 все числа под индексом, кратным 3

list1 = [1,4,78,3,7,0,4,2,7]
for ind in range(len(list1)):
    element = list1[ind]
    if ind%2: #ind%2 !=0
        list1[ind]=element*2
    if ind%3==0: #not ind % 3
        list1[ind]=element*3

print(list1)

list1 = [1,4,78,3,7,0,4,2,7]
for ind, element in enumerate(list1):
    if ind%2: #ind%2 !=0
        list1[ind]=element*2
    if ind%3==0: #not ind % 3
        list1[ind]=element*3

print(list1)

dict_={}
string='abcdefgh'
for k,v in enumerate(string,1):
    dict_[k]=v

print(dict_)

print(dict(enumerate(string,1)))

#zip

string1 = 'abcdefgh'
string2 = 'abcdefgh'
string3 = 'abcdefgh'
print(dict(zip(string1,string2)))

"===========================Функция высшего порядка===================="
# это функция, которая принимает в аргументы другую функцию
# возвращает функцию
# создает внутри себя функцию 
# вызывает внутри себя функцию

#map - принимает в аргументы функцию и итерируемый обьект.
#возвращает генератор, в котором все элементы - результат принимаемой функции,
#в которую передали элементы последовательности

mapped = map(int,['1','2','3'])
print(list(mapped)) #[1, 2, 3]

list1 = [1,2,3,4,5,6]
def res1(i):
    return i+1
print(list(map(res1,list1))) #[2, 3, 4, 5, 6, 7]

print(list(map(lambda i: i+1,list1))) #[2, 3, 4, 5, 6, 7]

#filter - функция которая принимает в аргументы функцию и итерируемый обьект.
# возвращает генератор, в котором элементы из последовательности
# прошедшие фильтр (функция вернула True)
list1 = [-3,7,0,34,-23,435,10]
def is_positive(x):
    return x>0
print(list(filter(is_positive,list1))) #[7, 34, 435, 10]

print(list(filter(lambda x: x>=0, list1))) #[7, 0, 34, 435, 10]

list2=['Hdsad','wOrld','asdasd','MAKERS']

print(list(filter(lambda x: x[0].isupper(),list2)))

# reduce - функциякотораяимпортируется из functools.
#тоже принимает функцию и итерируемый обьект.
# возвращает один 1 результат
from functools import reduce

list1 = [2,4,6,3,65,8]

def mul(x,y):
    return x*y
res = reduce(mul,list1)
print(res) #74880
print(reduce(lambda x,y:x*y,list1))

list1 = 'hello'

print(reduce(lambda x,y:x+"$"+y,list1)) #h$e$l$l$o

list_ = ['hello','world','makers','bootcamp','asa']


def isbigger(x,y):
    if len(x)>len(y):
        return x
    return y
    
print(reduce(isbigger,list_))
print(reduce (lambda x,y:x if len(x)>=len(y) else y,list_))
print(dir(list_))


a=[1,2,3,4]
b=str(a)
print(b[0])
print(type(b))





    
