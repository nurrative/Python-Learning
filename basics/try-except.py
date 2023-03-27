"=============================Exception===================="
#  Исключения (ощибки) - обьекты, которые обрабатывают работу кода,
#  если не были обработаны

SyntaxError
# исключение, которое выходит если допущена синтаксическая ошибка
"""
(
SyntaxError: '(' was never closed
"""
# если используем ключевы слова не правильно
"""
break
SyntaxError: "break"
"""
TypeError
#  исключение, которое выходит когда мы делаем что-то несвойственное 
# данному типы данных
"""
1+'1'
"""
# когда мы передаем в функцию больше или меньше аргументов, чем она требует

KeyError
# когда мы обращаемся по несуществующему ключу
"""
dict_{'a':1,'b':2}
dict_['c']

KeyError: 'c'
"""

NameError
# если нет такой пременной

ValueError
# когда мы передаем в функцию, то что она не может корректно обработать
# когда мы пытаемся распаковать не такое же количество элементов в несколько переменных
"""
a,b=1,2,3
a,b,c = 1,2
ValueError: too many values to unpack(expected 2)
"""

AttributeError
# когда пытаемся обратиться к несуществующему методу в каком-то типе данных
"""
list_=[]
list_.lower()
AttributeError: 'list' object has no attribute 'lower'
"""

IndexError
# когда обращаемся по несуществующему индексу
"""
list1=[1,2,3]
list1[100]
IndexError: list index out of range
"""

ModuleNotFoundError
# когда обратиться к несуществующей библиотеке
"""
import django
ModuleNotFoundError: No module named 'django'
"""

ZeroDivisionError
# когда делим на 0
"""
IndentationError
 v=10

if True:
print('Hello') 
IndentationError: expected an indented block after 'if' statement on line
"""

Exception
# исключение, которое создали чтобы его вызывать

# чтобы вызывать исключения, используем  raise
# raise Exception

"===========================Обработка исключений========================"

try:
    # код, который возможно вызовет ошибку
    num = int(input("Введите число: "))
except ValueError:
    # код, который обрабатывает только если в блоке try вызвалась ошибка ValueError
    print("Вы ввели не число")    
else:
    # код , который обработает только если в блоке try ни одна ошибка не вызвалась
    print("Введенное число", num)
finally:
    # код,который обрабатывает в любом случае, хоть вызвалась ошибка,
    # хоть не вызвалась ошибка 
    print("До свидания")    
# минимальная конструкция состоит из try-except или try-finally 
# можно использовать несколько except
try:
    num1=(int(input("Введите первое число: ")))
    num2=(int(input("Введите второе число: ")))
    print(num1//num2)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("Нельзя делить на 0")   

try:
    print(1+'1')
except TypeError:
    print(int())         

dict_ = {'key1': 'value1', 'key2': 'value2'} 
try:
    print(dict_.get('value2'))
except:
    print("Нет такого ключа!")    
