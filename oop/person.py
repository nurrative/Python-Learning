class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    class Woman:
        pass
class Developer(Person):
    def __init__(self,name,age,developer):
        
        super().__init__(name,age)
        self.developer = developer
        
        print(f"Имя {self.name} Возраст: {self.age} Разработчик: {self.developer}" , )

    def move(self):
        print("хожу")


developer1 = Developer("Marat", 20,"Backend")
developer1.move()

class A:
    _name='aasd'

class B(A):
    pass

class C(B):
    pass

c = C()

print(c._name)

