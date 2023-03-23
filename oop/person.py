class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Developer(Person):
    def __init__(self,name,age,developer):
        
        super().__init__(name,age)
        self.developer = developer
        
        print(f"Имя {self.name} Возраст: {self.age} Разработчик: {self.developer}" , )


developer1 = Developer("Marat", 20,"Backend")
# developer2 = 
