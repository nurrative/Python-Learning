# class A:
#     def public(self):
#         return 'Public method'
#     def _protected(self):
#         return 'Protected method'
#     def __private(self) :
#         return 'Private method'

# obj1 = A()
# print(obj1.public)
# print(obj1._protected)
# print(obj1._A__private)

# class Car:
#     def __init__(self,speed=0):
#         self.__speed = speed
    
#     def set_speed(self,new):
#         self.__speed = new
    
#     def show_speed(self):
#         return self.__speed

# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 

# class Car: 
#     __speed=0
#     @property 
#     def speed(self): 
#         return self.__speed 
#     @speed.setter 
#     def speed(self,new): 
#         self.__speed=new 
#         return self.__speed 
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed) 

# class Person:
#     name="John"
#     _phone_number="+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(Person._Person__card_number)

# class Person:
#     def __init__(self, name, phone_number, card_number): 
#         self.name = name
#         self._phone_number = phone_number 
#         self.__card_number = card_number 

#     def get_card_number(self):
#         return self.__card_number

# john=Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(john.name)
# print(john._phone_number)
# print(john.get_card_number())

# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number =  "9999 9999 9999 9999"
#     @property 
#     def number(self): 
#         return self.__card_number 

# john = Person()
# john.name = None
# john._phone_number = None
# john._Person__card_number = None
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)

# class Person:
#     def __init__(self, name, phone_number, card_number): 
#         self.name = self.__validate_name(name) 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 
#     def __validate_name(self, name):
#         if len(name) < 2: 
#             return "John" 
#         else: 
#             return name.title() 
#     def get_card_number(self): 
#         return self.__card_number 
# sam = Person("SAM","+996 557 55 17 57","9999 9999 9999 9999")
# print(sam.name)
# print(sam._phone_number)
# print(sam._Person__card_number)


# class Person:
#     def __init__(self, name, phone_number, card_number): 
#         self.name = name 
#         self._phone_number = self._validate_phone_number(phone_number) 
#         self.__card_number = self.__validate_card_number(card_number)
#     def _validate_phone_number(self, phone_number):
#         if type(phone_number)!=int: 
#             return None
#         elif str(phone_number)[0:3]!='996': 
#             return None 
#         else:
#             return phone_number
#     def __validate_card_number(self,card_number): 
#         if len(str(card_number))==16:
#             return card_number
#         else:
#             return None
    
#     def get_card_number(self):
#         return self.__card_number

# tolik = Person("SAM",996557551757,9999999999999999)
# print(tolik.name)
# print(tolik._phone_number)
# print(tolik.get_card_number())

# class Game:
#     __level = 0
#     def __init__(self,name):
#         self.name = name

#     def play(self,hours):
#         if hours > 2:
#             self.__level += 1

#     def get_level(self):
#         return self.__level 
# game = Game("Nursultan")
# print(game.get_level())
# game.play(4)
# game.play(3)
# print(game.get_level())

# class Game:
#     __level = 0
#     def __init__(self,name):
#         self.name = name

#     def get_level(self):
#         return self.__level 

#     def set_level(self,number):
#         self.__level=number
# game = Game("Nursultan")
# print(game.get_level())
# print(game.set_level(10))
# print(game.get_level())

 
# class Game:
#     __level=0
#     def __init__(self,name):
#         self.name = self.__validate_name(name)

#     def set_level(self,x):
#         if self.name=="Tolik":
#             self.__level=x
#         else:
#             print(f"{self.name} ты не Tolik!")

#     def __validate_name(self,name):
#         return name.title()
    
#     def get_level(self):
#         return self.__level

# game = Game("Raychel")
# game.set_level(5)
# print(Game._Game__level)
# game2 = Game("Tolik")
# game2.set_level(5)
# print(game2._Game__level)

# class Game:
#     __level = 0
#     @property
#     def get_level(self):
#         return self.__level
#     @get_level.setter
#     def level(self,number):
#         self.__level=number
# game = Game()
# print(game.get_level)
# game.level=10
# print(game.get_level)

# class Person:
#     def __init__(self):
#         self.__name=None
#         self.__last_name=None
#         self.__age=None
#         self.__email =None
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def last_name(self):
#         return self.__last_name    
#     @property
#     def age(self):
#         return self.__age    
#     @property
#     def email(self):
#         return self.__email
#     @name.setter
#     def name(self,value):
#         self.__name = value
#     @last_name.setter 
#     def last_name(self, value): 
#         self.__last_name = value 
#     @age.setter 
#     def age(self, value): 
#         self.__age = value 
#     @email.setter 
#     def email(self, value): 
#         self.__email= value 

# john = Person()
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name,john.last_name,john.age,john.email) # John Snow 30 johnsnow@gmail.com

# class Dad: 
#     name = 'John' 
#     _last_name = 'Snow' 
#     __age = 40 

# class Dad: 
#     name = 'John' 
#     _last_name = 'Snow' 
#     __age = 40 

# class Me(Dad): 
#     name = 'Sam'
#     __age = 10 
#     def about_me(self): 
#         print(f"My name is {self.name} {self._last_name} and I am {self._Me__age} years old") 
#     def about_my_father(self): 
#         print(f"My father is {super().name} {super()._last_name}") 
# me = Me() 
# me.about_me() 
# me.about_my_father()



