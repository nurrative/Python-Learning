# Инкапсуляция
> Принцип ООП, у которого 2 трактовки
1. все, что нужно для работы класса - лежит в классе
2. соктырие данных (ограничение доступа к атрибутам)

## Виды доступа
1. public (публичные)
2. protected (защищенный) - один underscore в начале
3. private (приватный) - два underscore в начале

> В python инкапсуляция реализовано на уровне соглашения
```py
class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'
```
# Getters / Setters
> методы, с помощью которых мы указываем каким образом мы можем получать и изменять
какие-то атрибуты

```py
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age =age

    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        if new_age>0 and new_age<120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")

person1 = Person("Marat",22)
print(person1.name)
print(person1.get_age())
person1.set_age(145)
print(person1.get_age())
```

## Property
> декоратор, который превращает в атрибут с декораторами getter, setter, deleter

> setter будет вызываться, когда мы записываем в атрибут значение
> deleter будет вызываться, когда мы удаляем атрибут через del

```py
class A:
    @property #превратили функцию в атрибут
    def hello(self):
        return 5
    
    # property.setter работает когда мы пишем obj.attr = ...
    @hello.setter
    def hello(self,new_value):
        print('setter')
    
    # property.deleter работает когда мы пишем del obj.attr
    @hello.deleter
    def hello(self):
        print("deleter")
obj = A()
print(obj.hello)
obj.hello = 'new value'
del obj.hello
```

```py

