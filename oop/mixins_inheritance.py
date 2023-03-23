"""
1 Миксины - классы, которые будут использоваться для наследования
Но от миксинов не создаются обьекты
2 Миксины - классы-примеси, которые служат для расширения класса
"""
#  От миксинов нельзя создавать классы, поскольку - несамомтоятельная
#  классы. При наследовании миксины должны идти в первую очередь

class WalkMixin:
    def walk(self):
        print("я могу ходить")
class SwimMixin:
    def swim(self):
        print("я могу плыть")

class Human(WalkMixin, SwimMixin):
    name = 'человек'
    def talk(self):
        print('я могу говорить')

class FlyMixin:
    def fly(self):
        print('я могу летать') 

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'
class Duck(WalkMixin,SwimMixin, FlyMixin):
    name = 'утка'

"""
objects =[Human(), Fish(),Exocoetidae(), Duck()]
for obj in objects:
    # print(obj.name)
    attrs = ['fly','swim','walk','talk']
    for attr in attrs: 
        if hasattr(obj,attr):
            method = getattr(obj,attr)
            method() 

print(hasattr(obj,'fly')) -> есть ли метод у этого класса(1-обьект, 2-атрибут)

print(getattr(obj,'walk'))<bound method WalkMixin.walk of <__main__.Human object at 0x1030eded0>>
method = getattr(obj,'name')
str(method())
setattr(obj, 'new_attribute','hello world') -> создает атрибут со значением
"""
# hasattr - функция, которая принимает обьект и название атрибута. Возвращает True,
# если у обьекта есть такой атрибут(метод)
# getattr - функция, которая принимает обьект и название атрибута. Возвращает значение атрибута
# setattr - функция, которая принимает обьект, название атрибута и значение атрибута.
# Добаваляет в обьект новый атрибут или перезапишет одноименный атрибут





# obj.fly()
# obj.swim()
# obj.walk()
