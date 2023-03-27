# from package.test1 import hello
# from package.test2 import list2

"==========================Работа с файлами==========================="
# open - функция, которая позволяет открывать файлы в определенном режиме
# r - read (только для чтения)
# w - write (только для перезаписи, каждый раз при открытии очищает файл)
# a - append (только для до дозаписи, добавляется в конец)
# x - создает файл, но если файл есть - ошибка
# b - бинарный вид

"==============================Read================================="
file = open('test.txt','r')
# если такого файла нет - выйдет ошибка
# если не указать режим - откроется в режиме чтения
print(dir(file))

print('readable', file.readable()) #readable True - читаемый
print('writable', file.writable()) #writable False - нельзя изменять

print(file.read()) #cчитывает от начала до конца
print(file.read()) #'', потому что каретка в конце

file.seek(0) #перенос каретки в начало
print(file.read(5)) #считывает от начала до 5 индекса
print(file.read()) #считает с 5 индекса до конца

file.seek(0)
print(file.readline()) #"Hello\n"
print(file.readline()) #"World\n"

file.seek(0)
print(file.readlines(10)) #['Hello\n', 'World\n'] ???

file.seek(10) #10 - показывает где каретка
print(file.tell())

file.read()
print(file.tell()) #19

print(file.closed) #False
file.close() #! важно закрывать файлы
print(file.closed) #True проверяет файл закрыт или нет и выдает булевое значение
print(file.name) #test.txt - название файла

"=============================Write================================"
file = open('new_file.txt','w',)
# если файла нет - создает
# если есть - очищает
print('readable', file.readable()) #readable False- читаемый
print('writable', file.writable()) #writable True - нельзя изменять
file.write("Hello\n")
file.write("Makers")
file.writelines(['\nHello\n','World'])

file.seek(0)
file.write('aaa') #aaalo
# Makers
# Hello
# World


file.close

"===============================Append============================="
file = open('new_file2.txt','a')
file.write("Hello\n")
file.write("Hello\n")

file.seek(0)
file.write('New')

file.close

"========================Контекстный менеджер======================"
with open('test.txt') as f:
    f.read()
    print(f.closed) #False
print(f.closed) #True
