##1********python的迭代不仅可用在list或tuple，还可以作用在其他可迭代对象上

#dict迭代：
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
#注意：dict的储存不是按照list顺序，所以结果顺序可能不一样
#      dict默认迭代key
#迭代dict的value：
for value in d.values():
    print(value)
#同时
for k,v in d.items():
    print(k,v)

#字符串的迭代：
for ch in 'ABC':
    print(ch)



##2**********判断可迭代对象：
#通过collections模块的lterable类型判断：
from collections import Iterable
isinstance('abc',Iterable)          #instance实例；情况 #str是否可迭代
isinstance([1,2,3],Iterable)        #list是否可迭代
isinstance(123,Iterable)            #整数是否可迭代


##3*********若要对list实现类似java那样的的下标循环
#enumerate函数可以把list编成索引-元素对
for guess_data, value in enumerate(['A', 'B', 'C']):
    print(guess_data, value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)



##4******练习 ：
def findMinAndMax(L):
    if L ==[]:
        return (None,None)
    a = L[0]
    b = L[0]
    for x in L:
        if x>a:
            a=x
        if x<b:
            b=x
    return (b,a)
# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')
            
print(max(5,90))
