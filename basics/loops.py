"Циклы"
# цикл - блок кода, который обрабатывается несколько раз
# for - цикл, который работает с итерируемыми обьектами, цикл заканчивает
# свою работу, когда он доходит до последнего элемента в итерируемом обьекте

# while - цикл, который работает до тех пор, пока условие верное

# list1 = ['hello', 10, True, [1,2,3]]
# for element in list1:
#     print(element)
# print(element)

string1 = 'hello world'
for letter in string1:
    print(letter)

i=1
while i !=10:
    print('hello',i)
    i=i+1

i=0
while i:
    print("hello world")  #вообще ни разу не обрабатывает, потому что 0 это False
    i = i +1

"==============================Ключевые слова в циклах======================="
# break - полностью останавливает цикл
# continue - переход к следующей итерации
# for i in range(10):
#     if i==3:
#         break         #----> 0,1,2,
#     print(i)

# for i in range(10):
#     if i==3:
#         continue         #----> 0,1,2,4,5,6,7,8,9
#     print(i)    
list1 = [1,2,3,1,1,3,4,2,12,11,9,1] 
while i in list1:
    list1.remove(1)
print(list1)  

# list1 = [1,2,3,1,1,3,4,2,12,11,9,1] 
# list2=[]
# for i in list1:
#     if i!=1:
#         list2.
# print(list2)        