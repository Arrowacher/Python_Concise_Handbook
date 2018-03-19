##1******
#取list或tuple元素有很多方法
L=['Michael','Sarah','Tracy','Bob','Jack']
#例：取前三个元素
#笨方法：
print([L[0],L[1],L[2]])
#好一点的循环取：
n=3
r=[]
for guess_data in range(n):          #range(3):range(0,3):0,1,2
      r.append(L[guess_data])
print(r)
#对这种经常取指定索引范围的操作，用循环十分繁琐
#Python提供了切片（Slice）操作符，能大大简化这种操作。
print(L[0:3])               #一行解决0-3但不包括3
#L[0:3]==L[:3]
print(L[1:3])
#由于L[-1]为最后一个元素……
print(L[-2:])               #[L[-2],L[-1]]：-2到0，但不包括0
print(L[-2:-1])             #[L[-2]]：-2到-1，但不包括-1


##2*****好用的切片
L=list(range(100))  #0-99
print(L[:10])       #取出了前10个数
print(L[-10:])      #取出了后10个数
print(L[10:20])      #前11-20的数

#!#
#前10个数，每两取
print(L[:10:2])     #[0,2,4,6,8]
#所有数，每5取
print(L[::5])
#[:]复制
L[:]        #可以原样复制一个list
q=L
s=L[:]      #测试说明L[:]和L同等
print('q=',q)
print('L=',L)
print('s=',s)

#特殊#字符串也可直接看作list，每个字符就是一个元素
print('ABCDEFG'[:3])    #'ABC'
print('ABCDEFG'[::2])   #'ACEG'
print('ABCDEFG'[2:-2])  #'CDE'



##3*****练习
#我的垃圾方法：
def trim(s):
    a = 0
    b = len(s)                #取s的长度
    i = 0
    x = 0
    if s == '':               #s长度为0，直接返回
        return s
    while s[i] == ' ':        #全空格的处理
        i = i+1               
        a = i                 #记录空格数
        if i == b:            #如果全是空格，则……
            return ''
    i = -1
    while s[i] == ' ':
        b = i
        i = i-1
    s = s[a:b]                #显示去掉前后空格后的部分
    return s

#使用了递归的别人的方法：
##def trim(s):
##    if (len(s)==0):               #s长度为0，直接返回 
##        return ''
##    if(s[0]==' '):                #1.前部一个空格，改成调用s[1:]为目标
##        return trim(s[1:])        #2.最后会为空，从而返回''。
##    elif(s[-1]==' '):
##        return  trim(s[:-1])
##    else:
##        return s
# 测试:
if trim('hello   ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')




