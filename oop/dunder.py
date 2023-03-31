#dunder (double underscore) - методы у которых 2 _ в начале и в конце
# магия в том, что мы их не вызываем напрямую

class A:
    def __new__(cls):
        print('__NEW__')
        return super().__new__(cls)
    
    def __init__(self):
        print("__INIT__")
        pass

A()
# __new__,__init__ - вызываются при создании обьекта

print(object.__dir__)
"""
# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __add__ +
# __sub__ -
# __floordiv__ /
# __truediv__ //
"""
# __str__ str, print
class A():
    def __str__(self):
        return 'Hello'
    pass
print(A()) #<__main__.A object at 0x100d30e50>


"""Task 4"""
class Student:
    def __init__(self,name,class_name,ball):
        self.name=name
        self.class_name = class_name
        self.ball = ball
        self.average = sum(ball.values())/len(ball)

    def __gt__(self,other):
        return f'> {self.average>other.average}'
    
    def __lt__(self,other):
        return f'< {self.average<other.average}'

    def __ge__(self,other):
        return f'>= {self.average>=other.average}'

    def __le__(self,other):
        return f'<= {self.average<=other.average}'

# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88}) 

# print(obj_student1 > obj_student2)
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2) 

# class Word:
#     def __new__(cls,string):
#         cls.string = "".join(string.split(" "))
#         return cls.string


#     def __gt__(cls,other):
#         if len(cls.string)>len(other.string):
#             return True
#         else: return False
    
#     def __lt__(cls,other):
#         if len(cls.string)<len(other.string): 
#             return 

#     def __ge__(cls,other):
#         return f'asd {len(cls.string)>=len(other.string)}'

#     def __le__(cls,other):
#         return f'{len(cls.string)<=len(other.string)}'
    


# class Kopilka:
#     def __init__(self):
#         self.__total = 0
#         self.__coins = []

#     def add_moneta(self,moneta):
#         self.__total+=1
#         self.__coins.append(moneta)

#     def __len__(self):
#         return self.__total
    
#     def __getitem__(self, index):
#         return self.__coins[index]

# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30)
# print(len(obj))
# for i in obj: 
#      print(i) 

# class Anagram(str):
#     def __init__(self,string) -> None:
#         self.string = string
#         print(self.string[-1:])
#     def __eq__(self,other):
#         if self.string[-1]==other.string:
#             return True
#         else:
#             return False
        
# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2)

h='hello'
print(h[-1:-5])