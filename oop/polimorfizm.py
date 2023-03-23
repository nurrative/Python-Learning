class Dog:
    def speak(self):
        print('гав-гав')

class Cat():
    def speak(self):
        print('мяу-мяу')

class Frog():
    def speak(self):
        print('ква-ква')

animals = [Cat(),Frog(),Dog(),Cat(),Dog(),Frog()]
for animal in animals:
    animal.speak()
    
list1 = [1,2,3,4,5]
dict1 = {'a':1,'b':2}

list1.pop(0) #удаление по индексу
dict1.pop('a') # удаление по ключу

# __add__
a = 4
b = 5
print(a+b)
print(a.__add__(b))
#  в списке add новый создает, extend расширяет старый
a = [1,2,3]
b = [4,5,6]
print(a.__add__(b))
print(a)
#__len__ - дандер метод
print(len(a))
print(a.__len__())