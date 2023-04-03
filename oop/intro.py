class Person:
    # переменные внутри класса-атрибуты
    arms = 2
    legs = 2


    #функции внутри класса - методы
    def __init__(self,name) -> None:
        print("asd")
        # __init__ -dunder метод, который добавляет в обьект self 
        # атрибуты которые отличаются у разных обьектов 
        self.name = name

    def walk(self):
        # self - ссылка на обьект, у которого мы вызываем данный метод
        # print(self) 
        print('я хожу') 

person1 = Person('Nursultan') 
# print(dir(str))
# print(dir(person1))
# print(__name__)
person1.walk()
# Person.walk(person1)

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name,p2.name,p3.name)

# print(dir(Person))
# print(dir(object))
# person1 = Person('Nursultan')
# person2 = Person('Sultan')

# print(person1.name,person2.name)

"""Атрибуты класса и атрибуты обьекта"""

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная обьекта'

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', 'var']
obj = A()
print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', 'var', 'var2']

# A.var2
# AttributeError: type object 'A' has no attribute 'var2'. Did you mean: 'var'
print(A.var1) #переменная класса
print(obj.var1) #переменная класса
print(obj.var2) #переменная обьекта

# def make_bold(func):
#     return f'<b>{func()}</b>' 


# def make_italic(func):
#     return f'<i>{func()}</i>'


def make_underline(func):
    string=(f"asd{func()}")
    return string

# @make_bold
# @make_italic
@make_underline
def hello():
    return 'Hello world'
 
print(hello())