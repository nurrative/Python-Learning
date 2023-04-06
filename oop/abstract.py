from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    pass

# obj = Dog()
# print(obj) Can't instantiate abstract class Dog 
# with abstract method speak

class Dog(AbstractAnimal):
    def speak(self):
        print("гав-гав")

obj = Dog()
obj.speak()

from abc import ABC,abstractmethod
class Coder(ABC):
    count_code_time = 0
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def coding(self):
        pass

class Backend(Coder):
    def __init__(self,experience, languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend

    def coding(self,hour):
        self.hour = hour
        self.count_code_time +=hour

        return self.hour
    def get_info(self):
        return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.hour} часов на программирование"

class Frontend(Coder):
    def __init__(self,experience,languages_frontend):
        self.experience = experience
        self.languages_frontend = languages_frontend

    def coding(self,hour):
        self.hour = hour
        self.count_code_time = hour
        return self.hour
    def get_info(self):
        return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.hour} часов на программирование"

class Fullstack(Backend,Frontend):
    pass

a=Backend("Junior","Python")
a.coding(12) 
print(a.get_info())

NotImplementedError

