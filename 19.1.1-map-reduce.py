##1******map(函数，Iterable)
#map将传入 的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)        #F,是Iterator!
print(next(r))
print(list(r))  #list()计算全部Iterator并返回一个list

##2*******map()是高阶函数
ssttrr = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(ssttrr)


##3*****reduce:把两个参数的函数作用在一个序列上
#reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
#例如：对一个序列求和：
from functools import reduce
def add(x,y):
    return x+y

s = reduce(add,[1,3,5,7,9])
print(s)

#例如：把序列[1,3,5,7,9]变成整数13579
from functools import reduce
def fn(x,y):
    return x*10+y

s = reduce(fn,[1,3,5,7,9])
print(s)

#>#配合map：str转int
from functools import reduce
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

reduce(fn, map(char2num, '13579'))  #str也是序列

#>>#整理成一个str2int
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

#》#进一步简化：使用lambda
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))


##4******练习：输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
#优秀参考：
##def normalize(name):
##    if not isinstance(name, str):
##        raise TypeError('Wrong Type')
##    elif name == '':
##        return ''        
##    elif len(name) > 1:
##        return name[0].upper() + name[1:].lower()
##    return name[0].upper()
#优秀参考：
##def normalize(name):
##    return name.title()
def normalize(name):
    n=0
    l=len(name)
    if l>1:
        return name[0].upper() + name[1:].lower()
    
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


##5*******练习：接收一个list并用reduce求积
def prod(L):
    def fx(x1,x2):
        return x1*x2
    return reduce(fx,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


##6*******练习：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
DIGITS ={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2float(s):
    n = 0
    for i in s:               #dev = s.find('.')
        if i == '.':          #
            break             #
        n += 1                #
    L1=s[:n]                  #s=s[:dev]+s[dev+1:]
    L2=s[n+1:]                #
    s=L1+L2
    c=pow(10,len(s)-n)
    print('c=',c)
    return reduce(lambda x,y:x*10+y,map(char2num,s))/c
#测试：
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

