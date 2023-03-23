#  class/static/instance methods
> **instance method**  - методы, которые первым аргументом принимает обьект от класса(instance,sуда). используются они для работы с обьектом и его атрибутами

```py
class A:
    def instance_method(self):
        print("метод обьекта")
        print('self', self)

obj = A()
obj.instance_method()
```

> **class methods** - методы, которые первым аргументом принимает класс (cls). используются они для работы с обьектом и его атрибутами
```py
class A:
    @classmethod
    def class_method(cls):
        print('метод класса')
        print('cls',cls)

obj = A()
A.class_method()
# метод класса
# cls <class '__main__.A'>
obj.class_method()
# метод класса
# <class '__main__.A'>
```

> для создания class метода, нужно использовать декоратор `classmethod` 

> **static method** - методы, которые не взаимодействуют с обьектом и классом, но находится внутри класса(по принципу инкапсуляции(все))
