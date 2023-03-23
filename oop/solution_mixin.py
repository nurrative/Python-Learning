# class RadioMixin:
#     def play_music(self,title):
#         print(f"Песня называется {title}")

# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')

# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')

# class  Amphibian(Auto,Boat):
#     pass
# obj = Amphibian() 
# auto = Auto()
# boat = Boat()
# auto.play_music("Dirty")
# boat.play_music("Amsterdam")
# obj.play_music("Umbrella")

# from datetime import datetime
# class Clock:
#     def current_time(self):
#         self.time= datetime.now().time().replace(microsecond=0)
#         print(self.time)

# class Alarm:
#     def on(self):
#         print('Будильник включен')
#     def off(self):
#         print('Будильник выключен')
    
# class AlarmClock(Clock,Alarm):

#     def alarm_on(self):
#         return super().on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()
class Coder:
    count_code_time = 0
    def get_info(self):
        model = self.__class__
        
        print(f"{model} разработчик, уровень: {model(self.experience())}, потрачено {Coder.count_code_time} часов на программирование")
    def coding(self,experience):
        model = self.__class__
        self.experience = experience
        Coder.count_code_time = self.experience
        return Coder.count_code_time
    def __str__(self):
        return Coder.model()
    
class Backend(Coder):
    def __init__(self,experience,languages_frontend):
        self.experience = experience
        self.experience = super().get_info()
        self.languages_frontend = languages_frontend
    def __str__(self):
        return self.experience

class Frontend(Coder):
    def __init__(self,experience,languages_frontend):
        self.experience = experience
        self.experience = super().get_info()
        self.languages_frontend = languages_frontend

class Fullstack(Backend,Frontend):
    def __init__(self,experience,languages_frontend):
        super().get.info()
        self.experience = experience
        
        self.languages_frontend = languages_frontend
    

a = Backend("Junior","Python")
# b = Frontend("Middle","Javascript")
# c = Fullstack('Senior','Python and JS')
print(repr(a.coding(12))) 
# b.coding(45) 
# c.coding(17) 

# from abc import ABC, abstractmethod

# class A(ABC):

#     @abstractmethod
#     def a(self):
#         pass


# class B(A):
#     pass

# b = B()
# print(b.a())

# class Square():
#     def __init__(self,side):
#         self.side = side
#     def get_area(self):
#         square = pow(self.side,2)
#         return int(square)
        

# class Triangle():
#     def __init__(self,height,base):
#         self.height = height
#         self.base = base
#     def get_area(self):
#         square = (self.height*self.base)/2
#         return int(square)
    

# class Pyramid(Triangle,Square):
#     def __init__(self,height,base):
#         super().__init__(height,base)
#     def get_volume(self):
#         volume = (1/3)*pow(self.base,2)*self.height
#         return int(volume)
    
# b = Pyramid(10,10)
# print(b.get_volume())

# class ExtensionMixin:
#     def add_extension(self,string):
#         model = self.__class__
#         obj = model(self.name,self.type,self.extensions)
#         obj.string =string
        
#         self.extensions.append(obj.string)
#         return f"Добавлено новое расширение {obj.string} для игры {self.name}."
#     def remove_extension(self,string):
        
#         model = self.__class__
#         obj = model(self.name,self.type,self.extensions)
#         obj.string = string
#         if obj.string in self.extensions:
#             self.extensions.remove(obj.string)
#             return f"{obj.string} был отключен от {self.name}"
#         else:
#             return "Такого расширения нет в списке."
# class Game(ExtensionMixin):
#     def __init__(self,type,name,extensions=[]) -> None:
#         self.type = type
#         self.name = name
#         self.extensions = extensions

#     def get_description(self,description):
#         self.description = description
#         return f"{self.name} это {self.description}"
#     def get_extensions(self):
#         if len(self.extensions)==0:
#             return 'Нет подключенных расширений'
#         else: 
#             string=''
#             for i in self.extensions:
#                 string += i+" "
#         return string

# game1 = Game('asd',"Minecraft")


