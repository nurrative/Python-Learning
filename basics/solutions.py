# hashtags = '#makers#bootcamp#программирование#it#курсы'
# res = hashtags.lstrip('#').split('#')
# print(res)
# string1 = "America"  
# string2 = "Japan"
# string3 = string1[:1] + string2[:1] + string1[3:4] + string2[2:3] + string1[-1] + string2[-1]
# print(string3)
# string1 = "America"  
# string2 = "Japan"
# string3 = string1[:1] + string2[:1] + string1[(len(string1)/2)-1:len(string1/2)] + string1[(len(string2)/2)-1:len(string2)/2] + string1[-1] + string2[-1]
# print(string3)
# import math
# string1 = "America"
# string2 = "Japan"
# len_str1 = math.floor(len(string1)/2)
# len_str2 = math.ceil(len(string1)/2)
# len_str3 = math.floor(len(string2)/2)
# len_str4 = math.ceil(len(string2)/2)
# string3 = string1[:1] + string2[:1] + string1[len_str1:len_str2] + string2[len_str3:len_str4] + string1[-1] + string2[-1]
# print(string3)
# x=32
# y=32
# z=32

# if x==y and x==z:
#     print('3')
# elif x==y or x==z:
#     print('2')  
# else:   print('0')   

# year = int(input())
# print()
# if year%4 !=0 or (year%100 ==0 and year%400 !=0):
#     print("NO")      
# else: print("YES")  
# string = 'Makers bootcamp'
# print(string[1::2])
# count = 0
# number = input()
# count = int(number)
# print(count)
# n = int(input())

# if n % 10 == 1 and n != 11:
#     print(f"На лугу пасется {n} корова")
# elif 2 <= n % 10 <= 4 and n // 10 != 1:
#     print(f"На лугу пасется {n} коровы")
# else:
#     print(f"На лугу пасется {n} коров")
# a =int(input())
# b=int(input())
# c =int(input())
# if a<b+c and b<a+c and c<a+b:
#     if (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b) :
#         print("rectangular")
#     elif (a*a>b*b+c*c) or (b*b>a*a+c*c) or (c*c>a*a+b*b):
#         print("obtuse") 
#     elif (a*a<b*b+c*c) or (b*b<a*a+c*c) or (c*c<a*a+b*b):
#         print("acute")    
# else: print("impossible")        
# num = int(input())
# my_unicode = chr(num)
# if 65 <= num <=90 or 97<= num<= 122:
#     print('Это буква ' +chr(num))
# else: print("Это не буква, а символ "+ chr(num))    
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))

# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#     if abs(x1 - x2) == abs(y1 - y2):
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")
# count= 0
# number =input()
# if number.isdigit():
#     count = int(number)
#     if count>0:
#         print(count)
# else:
#     print(0)

# number = count
# print(count)

# name_of_list = ['Helloworld!']
# my_len = len(name_of_list[0][:])
# first_len = []
# second_len = []

# # print(name_of_list[0])
# if my_len%2==1:
    
#     first_len.append[name_of_list[0][0:my_len//2+1]]
#     print(first_len)
# my_list = []
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# for x in list_:
#     my_list.append(remove(x))
# print(my_list)  
"Task 22"
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lists.sort()
# max_list=lists[-1]
# min_list=lists[0]
# print("max_list "+str(max_list))
# print("min_list "+str(min_list))
'task19'
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8

# print(list_.count(x))

'task 31'
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# my_color = colors[:][::-1]
# print(my_color)

# lists = [ [1, 3],[0], [5, 7],  [13, 15, 17],[9, 11], [13, 15, 15]]
# my_list=[]
# for i in lists:
#     if len(i):
#         my_list.append(len(i))
# print(my_list)  

# # print(lists[my_list[0]])
# # print(lists[my_list[-1]])
# x=lists[my_list[0]]
# print(x)
# y=lists[(my_list[-1])+1]
# print(y)
# print(type(len(lists)))
list_ = ['dlrow', 'olleh']
res = [x[::-1] for x in list_[::-1]]
print(res)

result=[]
for i in list_[::-1]:
    result.append(i[::-1])
print(result)