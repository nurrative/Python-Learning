"==================================List========================="
#  спсок = это изменяемый, итерируемый, индексируемый и упорядоченный 
# тип данных предназначенный для хранения элементов в строгом порядке
list1 = [10, 3,5, 'hello', [], (1,2), None, True, False] #что угодно
list1[0] #10
list1[3] #[1,2,3]
list1[3][-1] #3
list1[-1] #False
list1[2][-1] # 'o'

list2 =lis2 = list("hello")
print (list2) #['h','e', 'l', 'l', 'o']

print(list(range(3,10,2))) # 3,5,7,9

"=============================изменяемость===================="
string = 'hello'
string.upper()
print(string) #hello -> не изменилась

list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print (list1) #1, 2, 3

"=======================Методы списков======================="
# append -> метод, который добавляет элемент в конец списка
list1 = []
list1.append('hello')
list1.append(500)
list1.append([1,2,3])
print(list1) # ['hello', 500, [1,2,3]]

#remove - метод который удаляет элемент из списка по значению,
# но только его первое вхождение элемента
list2 = [10, 'hello', 500, 'world', 1000, 'hello', 500]
list2.remove('hello')
print(list2) # [10, 500, 'world', 1000, 'hello', 500]

#pop -> метод который удаляет элемент по индексу
list3 = [10,20,30,40,50]
list3.pop()
list3.pop(1)

# также метод pop возвращает удаленный элемент
list4 = [10,20,30,40,50]
popped = list4.pop(0)
print(list4) # [20,30,40,50]
print(popped) # 10

# insert -> метод, который добавляет элемент в список по индексу
list5 = [1,2,3,4]
list5.insert(0,'hello')
print(list5) #['hello', 1, 2, 3, 4]

list6 = list(range(1,11))

# print(list6[::-1])
# print(list6.reverse())
# print(list(reversed(list6)))
list
