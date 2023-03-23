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

