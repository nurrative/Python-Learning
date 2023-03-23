# class A:
#     def method(self):
#         print("Метод в классе А")

# obj_a = A()
# obj_a.method()
# # "Метод в классе А"

# class B(A):
#     pass

# obj_b = B()
# obj_b.method()

# class C(A):
#     def method(self):
#         print("Метод в классе С")

# obj_c = C()
# obj_c.method()
# "Метод в классе C

class A():
    def method(self):
        print("Метод в классе А")
        return "AAA"

class B(A):
    def method(self):
        print("Метод в классе B")
        return_from_super = super().method()
        print("super().method() вернул", return_from_super)
        return "BBB"
obj_a = A()
res_a = obj_a.method()
print('A.method вернул', res_a)

obj_b = B()
res_b = obj_b.method()
print('B.method вернул', res_b)

class Range:
    def create(self,n):
        """Принимает число и возвращает список чисел от 0 до данного числа
        включительно"""
        return list(range(n+1))

num1 = Range()
print(num1.create(5))

class Range10(Range):
    def create(self):
        """Создает range от 0 до 10 включительно"""
        return super().create(10)

num2 = Range10()
print(num2.create()) 

#Виды наследования 
class A:
    attr1='a'
    def method(self):
        print("Метод в классе А")

obj_a = A()
obj_a.method()
# "Метод в классе А"

class B:
    attr2 = 'b'
    def method(self):
        print("Метод в классе B")


class C(A,B):
    pass

obj_c = C()

print(obj_c.attr1) #a
print(obj_c.attr2)  #b
obj_c.method() #Метод в классе А

print(C.mro())
#[<class '__main__.C'>, <class 'A'>, <class 'B'>, <class 'object'>]


class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
# class E(C,D):
#     pass

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B

    

