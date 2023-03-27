"=====================================JSON========================================"
# JavaScript Object Notation - tдиный формат, в котором храниться только те типы 
# данных, которые есть во всех яп поддерживаемые json

#  числа int, float
# строки str
# словари dict
# булевые значения True, False
# списки list
# пустое значение None

import json

# сериализация - перевод из python в json
# dump
# dumps - функция, которая переводит python obj в json строку

python_list = [1,2,3]
json_list = json.dumps(python_list)
print(python_list) #list [1,2,3]
print(json_list) #str "[1,2,3]"

list_ = [
    1,2,3,
    4.6,
    (1,2,3),
    {'A':1},
    'hello',
    True,False,None
    #{1,2} TypeError: Object of type set is not JSON serializable
]
with open('test.json','w') as file:
    json.dump(list_,file)


# десериализация - перевод из json в python
# load
# loads


json_dict = '{"a":1,"b":2}'
python_dict = json.loads(json_dict)

print(type(json_dict)) #str
print(type(python_dict)) #dict

with open("test.json","r") as file:
    res = json.load(file)

print(res)