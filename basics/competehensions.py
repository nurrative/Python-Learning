"===============================Competensions============================"
list1 =[i for i in range(1,11)]
print(list1)

#результат for элемент in последовательность
# #результат for элемент in последовательность if фильтр

comprehension = (i for i in range(1,4))
# print(comprehension)
# <generator object <genexpr> at 0x10032d970>
#  генератор - итерируемый обьект, который не хранит в себе полностью
# все элементы последовательности, а генерирует их когда требуется

print(next(comprehension))#1
print(next(comprehension))#2
print(next(comprehension))#3
# print(next(comprehension)) #StopIteration

#next - функция, которая принимает в себя генератор, запрашивает следующий элемент
# у генратора и возвращает его

comprehension = (i for i in range(1,4))
print(list(comprehension))#[1, 2, 3]
print(list(comprehension))#[]

"=========================Синтаксический сахар======================"
#list comprehension
list_compr = [i for i in "Hello"]
# print(list_compr) ['H', 'e', 'l', 'l', 'o']

#dict comprehension
dict_compr = {i:str(i) for i in range(1,11)}
# print(dict_compr)
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'} 

#фильтр 
string = "Hello WorLD"
res = [i for i in string if i.islower()] 
print(res)

my_list = [i for i in range(1,11,) if i%2==0]
print(my_list)
my_list2=[]

my_list2 = [i for i in range (2,11,2)]
print(my_list2)    

my_list = [i*100 for i in range(1,11)]
print(my_list)

my_list = [i*5 for i in ["Hello"]]
print(my_list)

res = ["Hello" for i in range(5)]
print(res)

users = ['test1','test2','test3']
string="Hello" 
res = ["Hello "+i for i in users ]
res = [f"Hello {name}" for name in users]
print(res)
list_=[]
# for i in users:
#     res.append("Hello "+i)
# print(res)    
result =[[x for x in range(1,i+1)] for i in range(1,6)]
print(result)  

list1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
res = [i for inner_list in list1 for i in inner_list]#====?
print(res)
list1={}

result ={i:[x for x in range(1,i+1)] for i in range(1,6)}
print(result)  

# set compehenshion
set_comp = {x for x in range(10)}
print(set_comp)