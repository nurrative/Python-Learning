# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return(f'Название этой песни {self.title}')

#     def show_author(self):
#         return(f'Автор этой песни {self.author}')

#     def show_year(self):
#         return(f'Эта песня вышла в {self.year} году')

# song =Song("Happier than ever", "Billie Elish", 2021)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())
# class BankAccount:
#     balance = 0

#     def withdraw(self,minus):
#         # self.minus = minus
#         BankAccount.balance-=minus
#         print(f"Ваш баланс: {BankAccount.balance} сом")
#     def deposit(self,plus):
#         # self.plus = plus
#         BankAccount.balance += plus
#         print(f"Ваш баланс: {BankAccount.balance} сом")
# account = BankAccount()
# account.deposit(1000)
# account.deposit(2000)
# account.withdraw(500)
# print(account.balance)

# class Taxi:
#     def __init__(self,name,cost,cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self,num):
#         price=self.cost+self.cost_km*num
#         return f"Такси {self.name}, стоимость поездки: {price} сом"


# taxi1 = Taxi(name="Namba",cost=50,cost_km=22)
# taxi2 = Taxi(name="Yandex",cost=50,cost_km = 11)
# taxi3 = Taxi(name="Jorgo",cost=50,cost_km = 30)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  

# class Phone:
#     def __init__(self,name,last_name,phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")

# contact=Phone("John","Snow","996707707707")
# contact.get_info()

# class Salary:
#     percent = 8
#     def __init__(self,salary,experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         price = (Salary.percent*self.salary/100)*self.experience
#         return price
    
# obj = Salary(10000,10)

# print(obj.count_percent()) 

# class Nobel:
#     def __init__(self,category,year,winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#         # return category,year,winner

#     def get_year(self):
#         age = 2023-self.year
#         return f"выиграл {age} лет назад"

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# class Password():
#     def __init__(self,password):
#         self.password = password

#     def validate(self):
#         if not any(char.isdigit() for char in self.password):
#             print("Password should contain numbers too")
#         if not any(char.isalpha() for char in self.password):
#             print("Password should contain letters as well")
#         if not any(char in "@#&$%!~*" for char in self.password):
#             print("Your password should have some symbols.")
#         else:
#             print("Ваш пароль сохранен.")

#     def __str__(self):
#         return "*"*len(self.password)

# val1=Password("asdfghfghgh1!")
# val1.validate()
# print(val1)

# class Math:
#     def __init__(self,value):
#         self.value = value
#     def get_factorial(self):
#         factorial = 1
#         for i in range(2, self.value+1):
#             factorial *= i
#         return factorial
#     def get_sum(self):
#         x = sum([int(y) for y in str(self.value)])
#         return x
#     def get_mul_table(self):
#         string=''
#         for i in range(1,11):
#             string +=(f"{self.value} x {i} = {self.value*i}\n")
#         return string.strip()
# n = Math(11)
# print(n.get_factorial())
# print(n.get_sum())
# print(n.get_mul_table())

# class ToDo: 
#     instances=dict()
#     def __init__(self,string): 
#         self.string=string 
         
#     def give_priority(self,priority): 
#         ToDo.instances[priority]=self.string
#     def list_of_tasks(self): 
#         return sorted(ToDo.instances.items()) 
# var1=ToDo('ckelele') 
# var1.give_priority(2) 
# var2=ToDo('lelelele') 
# var2.give_priority(3) 
# var3=ToDo('HIOHOHO') 
# var3.give_priority(1) 
# print(var3.list_of_tasks())

# class Class1:
#     def first(self):
#         return 1
#     def second(self):
#         return 2

# class Class2(Class1):
#     def third(self):
#         return 3
#     def fourth(self):
#         return 4

# obj = Class2()
# print(obj.first())
# print(obj.second())
# print(obj.third())
# print(obj.fourth())

# class A:
#     def method1(self):
#         print("Основной функционал")

# class B(A):
#     def method1(self):
#         super().method1()
#         print("Дополнительный функционал")
    
# obj = B()
# obj.method1()

# class MyString(str):
#     def __init__(self, string):
#         self.string = string
#     def append(self,hello):
#         self.hello = hello
#         self.string = self.string+self.hello
#         return self.string
#     def pop(self):
#         result =self.string[-1]
#         self.string =  self.string[:-1]
#         return result
#     def __str__(self) -> str:
#         return self.string 

# example = MyString('String') 
# example.append('hello') 
# print(example) 
# print(example.pop()) 
# print(example) 

# class MyDict(dict):
#     def get(self,key):
#         if dict.get(self,key)==None:
#              return "Are you kidding?"
#         else: return dict.get(self,key)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 

# print(obj_dict.get('some_title')) 

# class MyDict(dict): 
#     def get(self, key): 
#         default = 'Are you kidding?' 
#         return dict.get(self, key, default) 
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))
# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"name:{self.name}, age:{self.age}")


# class Student(Person):
#     def __init__(self,name,age,faculty):
        
#         super().__init__(name,age)
#         self.faculty = faculty
#     def display_student(self):
#         print(f"name:{self.name}, age:{self.age}, faculty:{self.faculty}")

# obj_student = Student("Rick",21,'science')
# obj_student.display() 
# obj_student.display_student()

# class ContactList(list): 
#     def __init__(self, list_): 
#         self.list_ = list_ 
#     def search_by_name(self, name): 
#         a = [] 
#         for i in self.list_: 
#             if name in i: 
#                 a.append(i) 
#         return a 
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))
# from datetime import datetime
# class SmartPhones():
#     def __init__(self,name,color,memory,battery=0):
#         self.name = name
#         self.color= color
#         self.memory = memory
#         self.battery = battery
#     def __str__(self):
#         return f"{self.name} {self.memory}"
#     def charge(self,battery):
#         self.battery = battery
#         return self.battery
    
# class Iphone(SmartPhones):
#     def __init__(self,name,color,memory,ios):
#         super().__init__(name,color,memory)
#         self.ios = ios
#     def send_imessage(self,string):
#         self.string = string
#         return f"sending {self.string} from {self.name} {self.memory}"
# phone = SmartPhones('generic', 'blue', '128GB') 

# class Samsung(SmartPhones):
#     def __init__(self,name,color,memory,android):
#         super().__init__(name,color,memory)
#         self.android = android
#     def show_time(self):

#         self.time= datetime.now().time()
#         return self.time
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery)
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

# class Dog():
#     def voice(self):
#         print("Гав")

# class Cat():
#     def voice(self):
#         print("Мяу")

# barsik = Cat()
# rex = Dog()

# def to_pet(name):
#     return name.voice()

# to_pet(barsik) 
# to_pet(rex)

# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}"
    
# class Employee(Person):
#     def __init__(self,name,last_name,work,status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status
        

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}"

# class Student(Person):
#     def __init__(self,name,last_name,university,course):
#         super().__init__(name,last_name)
#         self.university = university
#         self.course = course
    
#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе"

# person= Person("Ivan", "Ivanov")
# employee = Employee("Ivan", "Ivanov","Рога и копыта", "директор")
# student = Student("Ivan", "Ivanov","КГТУ", 3)
# def get_human_info(name):
#     return name.get_info()
# print(get_human_info(employee))
# print(get_human_info(student))
# print(get_human_info(person))
# from abc import ABC, abstractmethod
# from math import pi
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 1/2*self.base*self.height

# class Square(Shape):
#     def __init__(self,length):
#         self.length = length
        
#     def get_area(self):
#         return pow(self.length,2)

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def get_area(self):
#         return pi*pow(self.radius,2)

# triangle = Triangle(5,5)
# square = Square(5)
# circle = Circle(10)
# print(triangle.get_area())
# print(square.get_area()) 
# print(circle.get_area())

class OS:
    def __init__(self,version):
        self.version = version

class Windows(OS):
    def __init__(self,version):
        super().__init__(version)
    def copy(self,text):
        self.text =text
        return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'

class MacOS(OS):
    def __init__(self,version):
        super().__init__(version)
    def copy(self,text):
        self.text =text
        return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'
class Linux(OS):
    def __init__(self,version):
        super().__init__(version)
    def copy(self,text):
        self.text =text
        return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'

class Language:
    def __init__(self,level,type):
        self.level = level
        self.type = type