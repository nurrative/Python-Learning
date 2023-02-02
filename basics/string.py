"==================================Строки==============================="
#строки - неизменяемый тип данных, предназначенный для хранения текста 
# (последовательности символов)
string1 = "строка в одинарных кавычках"
string2 = "строка в двойных кавычках"
string3 = "Don't"
string4 = ' Study in "Makers Incubator"'
string5 = '''
Многострочный 
текст
тут можно использовать любые кавычки
'''

"===========================Экранизация строк==========================="
# '\n' - перенос на новую строку
#  't' - отступ (табуляция)
# '\\' - отоброжение \ 
#'r'  -  'hello\rw' - wello
#'w'  - лесенка(перенос на новую строку со смещением вправо на длину новой строки)

"===========================Индексы==========================="
# индекс - это порядковый номер начиная с нуля
# index = len(string) - 1 or =string[-1]

# срез - часть строки
# string[6:9] wor из hello world  

"==============================Форматирование строк=============================="
# title = 'Пирог'
# price = 35
# string =f'Название: {title}, цена: {price}'
# format1 = 'Название: %s, цена: %s'
# print (format1 %(title, price))

# format2 = 'Название: {}, цена: {}'
# print(format2.format(title,price))

"==============================Методы строк=============================="
# метод - это функция которая принадлежит определенному типу данных
# обращаемся к ней через точку 
# dir(str)  - посмотреть все доступные методы для данного типа данных

'hello'.center(11) #'   hello   ' 
'hello'.center(11,-) #'---hello---' 
"""name = input()
last_name = input()
age = int(input())
city = input()
print(f"Вас зовут : {name} {last_name}, Ваш возраст: {age}, Вы проживатете в городе  {city}")


string = "Hello_world"
my_string = string[:5]+'K'+string[6:]
print(my_string)

string = 'MaKerS bOOtCamP'

string = 'hello world'
print((string+"\n")*3)

string = 'Makers'
# my_string = 'e'
print(string.find('e'))

string = 'Python is the best'
my_string = string.split(' ')
my_list = my_string[0]
if my_list == 'Python':
    print(True)
else: print(False)



string = 'Hello World ssssss'
my_str = string.split(" ")
if my_str[0:-1]=='':
    print(my_str[1:-2])
else :  
    print(my_str)

string = "          Как прекрасен этот мир!   "
print(.join(string.split()))
"""
