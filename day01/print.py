from random import random

print('hello python')
print('---------------------------')
a = 100
print(isinstance(a, int))
a = b = c = 1
print(a)
print(b)
print(c)
d, e, f = 1, 2, 'yes'
print(d)
print(e)
print(e)
print(f)

print('减法运算')
print(9 - 1)
print('除法运算')
print(8 / 3)
print('取余')
print(8 % 5)
str = 'hello'
print('从第一个到倒数第二个')
print(str[0: -1])
print('from index 0 to length - 2')
print(str[0: -2])
print('str length')
print(len(str))
print('str * 3')
print(str * 3)
list = [1, 2, 3, 4, 5, 6]
print(list[1])
print(list[0])
print(list)
sites = ['google', 'baidu', '360', 'alibaba']
print(sites)
if 'tencent' in sites:
    print('in here')
else:
    print('not here')
a = set('abcdefghigk')
b = set('efg')
print(a)
print(a - b)
print(int(1.00))
print(float(1))
a = 1
b = 1.0
c = 'test'
e = [1, 2]
dic = {}
dic[1] = 'python'
dic[2] = 'java'
print('a type is', type(a))
print('a type is ', type(b))
print('c type is ', type(c))
print('e type is ', type(e))
print(type(dic))
print(dic.values())
print(dic.keys())
print(dic.get(1))
print(random() * 100)
