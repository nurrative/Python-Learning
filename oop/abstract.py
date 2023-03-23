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