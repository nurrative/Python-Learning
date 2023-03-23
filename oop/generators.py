gen = (x for x in range(10))
# print(gen) #<generator object <genexpr> at 0x102d8c110>

def generator(n):
    for i in range(1,n+1):
        yield i**2
    
    
gen = generator(10)

print(gen)
# print(list(gen)) #[4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in generator(5):
    print(i)
# 1
# 4
# 9
# 16
# 25

gen = generator(15)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

#1 4 9 16 25 36 49 64 81 100 121 144 169 196 225

class IterInt(int):
    def __iter__(self):
        for i in str(self):
            yield int(i)

    def __len__(self):
        return len([i for i in self])
    
    def __getitem__(self,index):
        return [i for i in self][index]

a = IterInt(761253)
for i in a:
    print(i)

print(5 in a)
print(len(a))
print(a[0]) #7
print(a[1:4]) #[6, 1, 2]
print(a+1)

# print(dir(str))
string1 = 'abcdefafafwaf'
string2 = 'agydajd'
print(string1>string2) #False

class MyStr(str):
    # def __init__(self,string) -> None:
    #     self.string = string

    # def __len__(self):
    #     return len(self.string)
    
    def __eq__(self, other) -> bool:
        return len(self) == len(other)
    
    def __ge__(self, other) -> bool:
        return len(self) >= len(other)
    
    def __le__(self, other) -> bool:
        return len(self) == len(other)
    
    def __gt__(self, other) -> bool:
        return len(self) > len(other)
    
    def __lt__(self, other) -> bool:
        return len(self) < len(other)
    
    def __ne__(self, other) -> bool:
        return len(self) != len(other)

string1 =  MyStr('hel1lo')
string2 =  MyStr('asdqw')
print(string1>string2)

class A:
    attr1 = 'aaa'
    def __getattribute__(self, name):
        print('__getattribute__(name)', name)
        return super().__getattribute__(name) #__getattribute__(name) attr1
    
    def __setattr__(self,name,value) -> None:
        print("__setattr__",name,value)
        return super().__setattr__(name,value)
    
    def __delattr__(self,name) -> None:
        print('__delattr__',name)
        return super().__delattr__(name)


obj = A()
obj.attr1 ##__getattribute__(name) attr1
obj.attr1 = 'bbb' #__setattr__ attr1 bbb
del obj.attr1 #__delattr__ attr1
print(obj.attr1)