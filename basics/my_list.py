"task 20"
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]

# result = list(filter(lambda x: type(x) is int, list_))
# print(result)
# my_sum=0
# i=0
# while i<len(result):

#     my_sum=my_sum+result[i]
#     # print(i)
#     print(my_sum)
#     i=i+1
# # if result:
# #     print(*result)
# # else:
# #     print("нет там никаких цифр")

# print(my_sum)

# res = 0

# for i in list_:
#     if type(i) == int:
#         res+=i
#     elif type(i) == str:
#         if i.isdigit():
#             res+=int(i)
# print(res)
"task21"

# str_list = ['abc', 'xyz', 'aba', '1221']
# j=0
# my_list=[]
# len_index=5
# for i in str_list:
#     if len(str_list[j])>=2:
#         if str_list[j][0] == str_list[j][-1]:    
#             my_list.extend(str(j))    ==============>append?
#     j=j+1    
   
# print(my_list)




# "Task 25
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# str=input()
# my_list=[]
# for i in list_:
#     if i[0]==str:
#         my_list.append(i)

# print(my_list)
"Task 23"
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step = 3
# my_list = []
# for i in list_(0:15:i):
#     my_list.extend(i)
#     i=i+step

# print(my_list) 

'Task 30'
k = 3
zero = 0
my_list = []
for i in range(0,k):
    for j in range(0,k):
        my_list.append([0])
        print()