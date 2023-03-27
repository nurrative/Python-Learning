"============================Boolean Type==============================="
# у boolean типа всего 2 значения: True and False
# print(bool(1)) -> True
# print(bool(0)) -> False
# print(bool(-11)) -> True

# print(bool('hello')) -> True
# print(bool(' ')) -> True
# print(bool('')) -> False

# print(bool([])) -> False
# print(bool([[]])) -> True

"===============================None type================================"
#None - неизменяемый тиныпх с одним значением None,
# который используется для обозначения пустоты

# print(bool(None)) -> False
# print(bool('None')) -> True

"===========================Условные операторы==========================="
# условные операторы - это конструкция, которая используется для того, 
# чтобы  при разных входных данных код работал по-разному(в зависимости от условия)

# count= 0
# number =input()
# if number.isdigit:
#     count = int(number)
#     if count<0:
#         print(0)
#     else: print(count)
# else: print("none")    

count= 0
number =input()
if number.isdigit():
    number = int(number)
else:
    number = 0

number = count
print(count)