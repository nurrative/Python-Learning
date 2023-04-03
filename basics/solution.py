"Lists #6"
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []

# for x in nums:
#     if x<5:
#         res.extend([x])
# print(res)

"Lists #7"
# nums = input()
# list_ = []
# tuple_=tuple(nums[::2])
# for x in nums:
#     list_.extend([x])
# print(list_[::2])
# print(tuple_)

# nums = input()
# list_ = nums.split(",")
# tuple_=tuple(nums[::2])
# print(list_)
# print(tuple_)


"Lists #8"
# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     x = new_list.extend(str(x))=======>неправильный ответ
# print(new_list)

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     x = new_list.append(str(x))=======>правильный ответ
# print(new_list)

"Lists #9"
# list_ = [0,1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     if x%2==0:
#         new_list.extend(["even"])
#     if x%2==1:
#         new_list.extend(["odd"])
# print(new_list)        

"Lists #10"
# list_ = list(range(20))
# print(list_)

"Lists #11"
# list_ = list(range(0,101,2))
# print(list_)

"Lists #12"
# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# list1.extend(list2)
# sum=0
# print(list1)
# for x in list1:
#     sum=sum+x   ===================>sum+x
# print(sum)

"Lists #13"
# numbers = input()
# list_ = numbers.split(',')
# list_.sort()
# print(list_)

"Lists #14"
# list_=[3,1,2]
# if list_[0]!=list_[1] and list_[1]!=list_[2] and list_[2]!=list_[0]:
#     print("ERROR")
# else: print("yes")

"Lists #15"
# list_= []
# z=5
# my_list = list(range(54,9184))
# for a in my_list:
#     if a%z==0:
#         list_.append(a)
# print(list_)


# list_= []
# for i in range(54,9185):
#    if i % 5 == 0:
#        list_.append(i)
# print(list_)

"Lists #16"
# list_ = [20, 10, 20, 1, 100]
# list_.sort()
# print(list_[0])

"lists #18"
# fio1 = input().split()[-1]
# fio2 = input().split()[-1]
# fio3 = input().split()[-1]
# fio4 = input().split()[-1]
# fio5 = input().split()[-1]

# lists = [fio1, fio2, fio3, fio4, fio5]
# lists.sort()
# print(lists)

"List 19"
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8

# print(list_.count(number))
"Task 21"
# str_list = ['abc', 'xyz', 'aba', '1221']
# j=0
# my_list=[]
# for i in str_list:
#     if len(str_list[j])>=2:
#         if str_list[j][0] == str_list[j][-1]:    
#             my_list.extend(str(j))    ==============>append?
#     j=j+1    
   
# print(my_list)

"Lists #23"
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step = 3
# result = []
# for i in range(0, len(list_), step):
#     result.append(list_[i])
#     print(result)
# print(result)
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list=[]
# for i in range(step):
#     new_list.append(list_[i::step])
#     print(new_list)
# print(new_list)

# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step = 3
# result = []
# for i in range(step):
#     sub_list = []
#     for j in range(i, len(list_), step):
#         sub_list.append(list_[j])
#     result.append(sub_list)
# print(result)

"Task 24"
# size = 3
# matrix= []

# for i in range(size):
#     matrix.append([])
#     for j in range(1,size+1):
#         matrix[i].append(j)
"Task 25"
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany',
#           'abandon', 'cartoon']
# my_str = input()
# res=[]
# for i in list_:
#     if i[0]==my_str:
#         res.append(i)
        
# print(res)  

"Task 26"
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "blue", "green"]

# for i in colors1:
#     print(colors1)
#     for j in colors2:
#         if i==j:
#             colors1.remove(i)
#             colors2.remove(j)=================>не решенная
            
#         else: colors1
# print (colors1)
"Task 27"

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# for i in list1:
#     for j in list2:
#         if i==j:
#             print(True)
#             break
# else: print(False)
       
          
"Task 29"
# list_ = [1, 2, 3]
# for x in list_:
#     for y in list_:
#         for z in list_:
#             if x!=y and y!=z and z!=x:
#                 print((x,y,z))
"Task 30"
# K = 3
# matrix= []

# for i in range(K):
#     matrix.append([])
#     for j in range(K):
#         matrix[i].append(0)
# print(matrix)
"Task 31"            
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# my_color = []

# for i in colors:
#     my_color.append(i[::-1])
# print(sorted(my_color,key=len))

"Task 32"
# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# i = step

# while i <= len(list_):
#     list_.insert(i, element)
#     i = i + step + 1

# print(list_)

"Task 33"

"Task 34"    
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeat=1
# result=[]
# for c in list_:
#     if list_.count(c)>repeat and c not in result:
#         result.append(c)
# print(result)           


"======================================Dictionary====================="
#1
# a = {'x': 1, 'y': 2, 'z': 1}
# print(a['y'])

#2
# a = {'a': 1, 'b': 2, 'c': 1}
# deleted = a.pop('c')
# print(deleted)

#3
# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

#4
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

#5


#6
# a = {'a': 1, 'b': 2, 'c': 1}
# b=a.copy()
# print(b)

#7
# a = {'a': 1, 'b': 2, 'c': 1}
# for i in a:
#     print(i)

#8
# a = {'a': 1, 'b': 2, 'c': 1}
# for x,y in a.items():
#     print(y)

#9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for x,y in list(a.items()):
#     if y%2==0:
#         b[x]=2
#     else: b[x]=y    
# print(b)  

#10
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for x,y in list(a.items()):
#     if y==None:
#         a.pop(x)
# print(a)        

#11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# for x,y in list(a.items()):
#     a[x]=y/5
# print(a)

#12
# a = {'apple': 2, 'orange': 5, 'banana': 10}  
# for x,y in list(a.items()):
#     if y%2==0:
#         a.pop(x)
#     else: a[x]=y
# print (a)        

#13
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {}
# for key, value in list(a.items()):
#     b[value]=key
# print(b)    

#14
# a = {'a': 3, 'b': 2}
# num =0
# for key,value in list(a.items()):
#     num=num+value
# print(num)    

#15
# a1={'a': 1, 'b': 2, 'c': 3}
# a2 = a1.copy()
# a3={}

#16
# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.get('x'))

#17
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['b']
# print(dict_)   

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# key_to_delete = 'b'

# temp_dict = {}
# for key, value in dict_.items():
#     if key != key_to_delete:
#         temp_dict[key] = value

# dict_ = temp_dict

# print(dict_)

#18
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())

#19
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

# count = 0
# for x,y in list(dict_.items()):
#     if y>count:
#         count=y
# print(count)

#20
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# my_min=1000000
# for x,y in list(dict_.items()):
#     if my_min>y:
#         my_min=y
# print(my_min)        

#21
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for key,value in list(dict1.items()):
#     if value%2==1:
#         dict2[key]=1
#     else: dict2[key] = value
# print(dict2)  

#22
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for key,value in list(dict_.items()):
#     if value !=None:
#         dict_.pop(key)
# print(dict_) 

#23
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for key,value in list(dict1.items()):
#     dict2[key*key]=value
# print(dict2)    

#24
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for key in list_:
#     dict_[key]=len(key)
# print(dict_)  

#25
# dict_  = {'Makers': 6, 'coding': 6, 'hello': 5}
# str = ''
# count = 0
# for x,y in list(dict_.items()):
#     if y>count:
#         count=y
#         str = x
#     elif y==count:
#         str= str +" "+x    
# print(str)

#26
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for key,value in list(dict1.items()):
#     dict2[key]=pow(value,3)
# print(dict2)

#27
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for key1, value1 in dict_.items():
#     product=0
#     for val in value1.values():
#         product = val
#     dict_[key1]=product    
# print(dict_)        
#28
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for key,value in dict1.items():
#     product = 1
#     for val in value.values():
#         product *= val
#     dict2[key] = product
# print(dict2)

#29
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# my_num=[]
# my_str=[]
# for i in list_:
#     if type(i)==str:
#         my_str.append(i)
#     elif type(i)==int:
#         my_num.append(i)
# print(my_str)
# print(my_num)
# for x in my_str:
#     for y in my_num:
#         dict_[x]=y

# list1 = [1,2,3,4]
# list2 = ['a', 'b', 'c']
# res = dict(zip(my_str, my_num))
# print(res)
# ('hello', 23), ()
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# my_num=[]
# my_str=[]
# for i in list_:
#     if type(i)==str:
#         my_str.append(i)
#     elif type(i)==int:
#         my_num.append(i)
# res = dict(zip(my_str, my_num))
# print(res)

# print(dict_)
'''
list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']

my_num=[]
my_str=[]
for i in list_:
    if type(i)==str:
        my_str.append(i)
    elif type(i)==int:
        my_num.append(i)
dict_ = dict(zip(my_str, my_num))
print(dict_)
'''

#30
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # [0, 2, 1, 4, 3] ------>
# my_list = sorted(dict_, key=dict_.get)
# sorted_dict={}

# for my_key in my_list:
#     sorted_dict[my_key]=dict_[my_key]
# print(sorted_dict)

#31
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# my_list = sorted(dict_, key=dict_.get,reverse=True)

# for my_key in my_list:
#     sorted_dict[my_key]=dict_[my_key]
# print(sorted_dict)   

# 32
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = 5
# if key in dict_:
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = 5
# present = False
# for i in dict_.keys():
#     if i == key:
#         present = True
#         break
# if present:
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")  

# 33
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4={}
# dict4={**dict1, **dict2, **dict3}
# print(dict4)

# 35
# dict_ = {
#     'math': {
#         'sum': 
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }

# print(dict_['math']['sum'](dict_['vars'].values()))
# list1 = []
# for k,v in dict_.items():
#     for i_k, i_v in v.items():
#         if type(i_v) == int:
#             list1.append(i_v)
#         else:
#             summ = i_v

# print(summ(list1))

# sum()
 


#36
# a = {'a': 10, 'b': 9, 'c': 3}
# # b=list(a.values())
# # print(type(b))
# b=1
# for value in a.values():
#     b*=value
# print(b)    

#37
# string = "pythonist"
# dict_={}
# for i in string:
#     dict_[i]=string.count(i)
# print(dict_)    

# dict1 = {'a':1,'b':2,'c':3}
# dict2={ v:k for k,v in dict1.items()}
# print(dict2)

"=================================Try-Except===================="
# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_['key3'])
# except:
#     print("Нет такого ключа!")  

"Task6"
# list_ = [1, 4, 9, 16, 25, 36]
# try:
#     print(list_[7])
# except:
#     print('Нет такого элемента!')   

"Task 7" 
# try: 
#   age=int(input())
#   answer = age<=18
#   print(answer) 
# except ValueError as age: 
#   print("Введён некорректный возраст") 
# except ValueError as answer: 
#   print("Доступ запрещён") 
# finally: 
#   print("До свидания!") 

# try:
#     cash=int(input())
#     print(cash>=0)
# except ValueError:
#     print("Сумма не может быть отрицательной!")    

# try: 
#   age=int(input())
#   if age<18:
#         raise ValueError("Доступ запрещен")

# except: 
#   print("Введён некорректный возраст") 
# else:print("Спасибо")
# finally: 
#   print("До свидания!") 

# try:
#     age = int(input()) 
#     if age < 18: 
#         raise Exception('Доступ запрещён') 
# except ValueError: print('Введён некорректный возраст') 
# else: print('Спасибо') 
# finally: print('До свидания!')

# try:
#     string = input()
#     num = int(input())
#     sum=string+num
# except TypeError:
#     print("Unsupported option")  

   

# print("password")
# try: 
#     password = 'short' 
#     if len(password) < 6: 
#         raise ValueError
# finally:
#     print(password)

# warehouse = [['B', 's'], ['e', 'u'], ['O', 'o', 'x'], ['K', 'T'], [], [], [], [], [], []] 
# for i in warehouse: 
#     if len(warehouse)>10 or len(i)>3: 
#         raise ValueError()
         
# def to_fahrenheit(k:int)-> float:
#     assert k>=0,"Холоднее абсолютного нуля!"
#     temp = (k-273.15)*9/5+32
#     return temp

# print(to_fahrenheit(200))

# try:
#     import lamabimgo

# except ModuleNotFoundError:
#     print("Такого модуля нет")

# try:
#     def filter_comment(comment: str, banlist=[]) -> None:
#         comment_list = comment.lower().split(" ")

#         for i in comment_list:
#             if i in banlist:
#                 raise ValueError
            
# except ValueError:
#     print("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")

# filter_comment('Dis? recipe. is i !!UNLike!?!! really much!', ['hate', 'unlike', 'liken\'t'])
"""19"""
# try: 
#     num=100000000 
#     for i in range(0,num): 
#         print('Nope') 
# except KeyboardInterrupt: print('Nope')

"""20"""
# try:
#     inp1=input()
#     inp2=input()
#     print(int(inp1)+int(inp2))
# except TypeError:
#     print(inp1+inp2)

# except ValueError:
#     print(inp1+inp2)
"""21"""
# try:
#     inp=input()
#     list1=inp.split(" ")
#     list_=[]
#     for i in list1:
#         list_.append(int(i))
# except ValueError:
#     print("Данный элемент не является числом!")

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i',''):k.count('i') for k in dict1.keys()}
# print(dict2)



dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

# list_ = [value_inner['id'] for value in dict_.values() for value_inner in value['comments'] if len(value['comments'])>3]
# dict1 = [b['id'] for value in dict_.values() for b in value['comments'] if len(value['comments']) > 3] 
# print(list_)



dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

res = {k:k1 for k,v in dict_.items() for k1,v1 in v.items() if v1==max(v.values())}
print(res)

string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_=[x for x in string_.split(" ") if x.isdigit()]
print(list_)

