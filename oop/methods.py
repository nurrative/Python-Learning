'''
class A:
    def instance_method(self):
        print("метод обьекта")
        print('self', self)

obj = A()
obj.instance_method()
'''
# метод обьекта
# <__main__.A object at 0x102c90790>
# когда мы вызываем метод у обьекта, то нам не нужно передавать его в self, 
# он передается автоматически

# A.instance_method(obj)
#метод обьекта
# метод обьекта
# <__main__.A object at 0x102568790>
"""
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
"""
#  все равно от куда вы будете вызывать classmethod(от обьекта или класса), первым аргументом будет приходить class

#примеры 
class Counter:
    counter = 0

    def __init__(self):
        #обьект создается
        self._inc_counter()

    def __del__(self):
        # обьект удаляется
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        #cls - class C
        # увеличивает атрибут еласса на один
        cls.counter+=1

    @classmethod
    def _dec_counter(cls):
        cls.counter-=1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()
print(Counter.counter) #5
del obj1
print(Counter.counter) #4

class Pizza:
    def __init__(self,radius,*ingridients):
        self.r = radius
        self.ingridients = ingridients

    def cook(self):
        print(f"Пицца размером {self.r*2}")
        print(f"Ингридиенты: {self.ingridients}")

    @classmethod
    def four_cheese(cls,radius):
        pizza = cls(radius, "Мука","Сыр", "Колбаса","Cherry")
        #pizza = Pizza(20,"cheese1","cheese2","cheese3","cheese4")
        return pizza


pizza1 = Pizza(15,"Мука","Сыр", "Колбаса","Cherry")
pizza1.cook()
pizza2 = Pizza(20,"cheese1","cheese2","cheese3","cheese4")
pizza2.cook()

pizza4 = Pizza.four_cheese(10)
pizza4.cook()

pizza4 = Pizza.four_cheese(15)
pizza4.cook()

class A:
    @staticmethod
    def static_method():
        print("статик метод")

obj = A()
obj.static_method()

class Cylinder:
    def __init__(self,diameter, height):
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter,height)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h
        return circle_area*2+side_area
    
cylinder1 = Cylinder(4,10)
print(cylinder1.area) #150.79644737231007

print(Cylinder.get_area(4,10))

class A:
    def medthod1(self):
        print("Основной функционал")

class B(A):
    def medthod1(self):
        super().medthod1()
        print("Дополнительный функционал")

obj = B()
obj.medthod1()
        

class Product:
    base_price = 20000
    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color
    


    def has_garantiya(self,s_year):
        self.s_year = s_year
        res = s_year - self.year 
        if res>2:
            return 'Ваша гарантия истекла'
        else:
            return "Гарантия действительна"
        
    def change_price(self,change_price):
        Product.base_price = Product.base_price*change_price



obj = Product('A218', 2008, 'red') 
obj.change_price(2) 
print(obj.has_garantiya(2010)) 
print(obj.base_price) 

class User:
    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    @staticmethod
    def validate_email(email):
        return '@' in email

    @classmethod
    def create_user(cls, user_string):
        name, lastname, email = user_string.split(', ')
        return cls(name, lastname, email)

    def __str__(self):
        if self.validate_email(self.email):
            return f"{self.name}: {self.email}"
        else:
            return "email в неправильном формате"


user1 = User.create_user('John, Snow, john@gmail.com')
user2 = User.create_user('Alice, Smith, alice#smith.com')

print(user1)
print(user2)

class Makers:
    student_count=0
    def __init__(self,name,language,kpi):
        self.name = name
        self.language = language
        self.kpi = kpi

    @classmethod
    def new_student(cls,name,language,kpi):
        cls.student_count+=1
        return cls(name,language,kpi)
        
    def get_info(self):
        return f"Student name: {self.name}, Language: {self.language}"
    
    def set_kpi(self,kpi):
        self.kpi = kpi
        return self.kpi

student1 =Makers.new_student("Marat","JS",'89')
student2 =Makers.new_student("Oleg", "Python",'55')
print(student1.set_kpi(89)) 
print(student1.get_info()) 
print(student2.set_kpi(89)) 
print(student2.get_info()) 
print(Makers.student_count)

class Bike:
    def __init__(self,cost,make,model,year,min_profit,_sale_price = None,sold = False):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self._sale_price = _sale_price
        self.sold = sold
        self.min_profit = min_profit
    @classmethod
    def get_default_bike(cls):
        cost=10000
        make="Author"
        model="Basic ASL"
        year=2020
        _sale_price = None
        sold = False
        min_profit=2000
        print(min_profit)
        return cls(cost,make,model,year,min_profit,_sale_price,sold)
    
    def set_cost(self,price):
        self._sale_price = price

    def service(self,number):
        self._sale_price+=number

    def sell(self):
        self.sold = True
        price = self.cost-self.min_profit-self._sale_price
        return price
    
bike = Bike.get_default_bike() 
bike.set_cost(6000) 
bike.service(300) 
print(bike.sell()) 
print(bike.cost) 
print(bike.make) 
print(bike.year) 
print(bike._sale_price) 
print(bike.sold) 
print(bike.min_profit) 

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount
    
    def update(self, amount):
        self.amount = amount
        
    def __repr__(self):
        return str(self.amount)
        
    @staticmethod
    def dollarize(float_num):
        sign = "-" if float_num < 0 else ""
        integer_part = str(abs(int(float_num)))
        decimal_part = "{:.2f}".format(abs(float_num) - int(abs(float_num)))[2:]
        integer_part_list = list(integer_part)
        for i in range(len(integer_part_list) - 3, 0, -3):
            integer_part_list.insert(i, ",")
        return sign + "$" + "".join(integer_part_list) + "." + decimal_part
        
    def __str__(self):
        return self.dollarize(self.amount)
        
cash = MoneyFmt(1000000) 
print(cash.dollarize(-12.7801)) 

words =['apple','banana','date','elderberry']
short_words = list(filter(lambda x:len(x)>4,map(lambda x:x.upper(),words)))
print(short_words)


