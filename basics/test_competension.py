# "Task 3"
# # list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# # int_list = [i  for i in list_ if i>=0 and i%2==0 ]
# # print(int_list)

# "Task 4"
# list_ = [pow(i,2) for i in range(1,26)]
# print(list_)

# "Task 5"
# # str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# # int_str = [int(i) for i in str_list]
# # print(int_str)

# "Task 6"
# list_ = [i**2 if i%2==0 else i for i in range(1,11)]
# print(list_)

# "Task 7"
# list_ =[ True if i%2==0 else False for i in range(1,11)  ]
# print(list_)

# "Task 8"
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude']
# new_list = ['shorter' if len(i)<=4 else 'longer' for i in list_name ]
# print(new_list) 

# "Task 9"
# dict_ = {i:i**2 for i in range(1,11)}
# print(dict_)

"Task 10"
# number= int(input())
# dict1={key:key*key for key in range(number,501) if key%number==0}
# print(dict1)

"Task 11"
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}

# dict_={}
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key:[value for value in range(1,value+1)] for key,value in a.items()}    
# print(dict_)

# dict_={}
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key:list(range(1,value+1)) for key,value in a.items()}    
# print(dict_)

"Task 12"
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {key:'odd' if value%2==1  else 'even' for key,value in dict_.items()}
# print(a)

"Task 13"
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# my_list=string_.split(" ")
# list_ = [num for num in my_list if num.isdigit()]
# print(list_)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [word for word in string_.split() if word.isdigit()]
# print(list_)

"Task 14"
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict={key:max(value,key=value.get) for key,value in dict_.items()}
# print(new_dict)

"Task 15"

my_dict = {'first': {'a': 122}, 'second': {'b': 2}}
dict_={ key:list(value.values())[0] for key,value in my_dict.items()}
print(dict_)
"Task 16"
# list_ = [x for x in range(1,26) if x%2==0]
# print(list_)

"Task 17"
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [1 if x<0 else x for x in list_]
# print(int_list)

"Task 18"
# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [x for x in list1 if type(x)==str]
# print(list2)

"Task 19"
# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [x for x in list_ if x>5]
# print(list1)

"Task20"
# list_ = [False, True, False, True, False, True, False, True, False, True]
# my_list = [0 if i==False else 1 for i in list_]
# print(my_list)

"Task21"
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = [len(x) for x in list_name]
# print(new_list)

"Task 22"
# my_list = [x for x in range(1,1000,125) if x%2==0]
# print(my_list)

"Task 23"
# list1 = [44,54,64,74,104]
# list2 = [x+6 for x in list1]
# print(list2)

"Task 24"
# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [x for x in list1 if x*x>50]
# print(list2)

"Task 25"
# string = "happy birthday!"
# list_ = [x for x in string if x.isalpha()]
# print(list_)

"Task 26"
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}

# list_=[]
# for key,value in dict_.items():
#     num=0
#     for val in value.values():
#         num=val
#         list_.append(num)
# print(list_)    
# list_ = [val for key, value in dict_.items() for val in value.values()]
# print(list_)   
 
"Task 27"
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict_={key:pow(len(key),2) for key in list_name if len(key)>4 }
# print(dict_)

"Task 28"
'''
dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
  
list_ = [key.upper() for key,values in dict_.items() if 200<values<5000 ]
print(list_)
'''
# my_dict = {key.upper():value for key,value in dict_.items() if 200<value<5000}
# print(my_dict)
# my_dict = {}
# for key,value in dict_.items():
#     if 200<value<5000:
#         my_dict[key.upper()]=value
# print(my_dict) 

"Task 29"
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i',''):k.count('i') for k in dict1.keys()} 
# print(dict2)

"Task 30"

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [{x for x in list1 if x!=False}]
# print(list2)
# list2=[]
# for x in list1:
#     if 

"Task 31"
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers=[x[0] for x in SPL_Patrons if x[1]>100]
# print(readers)

"Task 32"
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# saved_amount =[round(x[1]*11.95,2) for x in SPL_Patrons]
# print(saved_amount)

"Task 33"
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# res = [[x[0],x[1]*42]for x in prairie_pirates if x[2]==True]
# print(res)

"Task 34"
# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# res = {v['likes'] for v in dict_.values() if v['rating'] > 3 }
# print(sum(res))



"Task 35"
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }
# dict1=[c['id'] for a,b in dict_.items() for c in b['comments'] if len(dict_[a]['comments'])>3] 
# print(dict1)
 
"Task 36"
# list_=[x/2 for x in range(0,11) if x%2==0]
# print(list_)

"Task 37"
# dict_ = {1:'Hello', 2:'world', 3:'python'}
# dict_ = dict({k:len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()})
# print(dict_)


"Task 38"
# set1 = {x for x in range(1,11)}
# set2 = {x for x in range(11, 21)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f'В этом сете было {20 - len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set) == 20:
#    print('Ваш объединенный сет полностью уникальный!')



