#一边循环一边计算的机制，称为生成器generator

#列表生成式：
L=[x*x for x in range(10)]
print(L)
#生成器：

g=(x*x for x in range(10))
print(g)        #无法打印元素
#可以通过next()
print(next(g),next(g),next(g),next(g))
#next()计算到最后一个元素，没有更多的元素时，StopIterration错误。

#或者for循环，因为generator也是可迭代对象
for n in g:         #不用担心StopIteration错误
    print(n)


##2******
#斐波拉契数列（1,1,2,3,5,8……）用列表生成式写不出来，但可以用函数
def fib(max):
    n,a,b = 0,0,1           #surprise！
    while n < max:
        print(b)
        a,b=b,b+a
        n = n + 1
    return'done'
fib(6)
#上面的函数和generator仅一步之遥。
#要把fib函数变成generator：只需把print(b)改为yield b.
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b             #yield 屈服；退位
        a,b = b,a+b
        n += 1
    return 'done'
#这是generator的另一种方法。若包含yield关键字，则就是generator：
f = fib(6)
print(f)        #显示错误：返回的是迭代器，所以需要for类语句输出。
next(f)         #注意：next()在Shell里才会显示


##yield()
#generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#例：
def odd():
    print('step 1')
    yield 'a'
    print('step 2')
    yield 2
    print('step 3')
    yield 3
#调用：先生成一个generator对象
o = odd()
##next(o)
##next(o)
##next(o)
##next(o)

#结果可知odd不是普通函数，而是generator！！！
#生成器执行过程中若遇到yield就中断，下次又继续执行。
    
for n in fib(6):
    print(n)
#for循环调用generator时，发现拿不到generator的return语句的返回值。
#要拿到返回值，捕获StopIteration错误，返回值包含在StopIteration的value中：
g=fib(6)
while True:                                         #默认循环
    try:
        x = next(g)
        print('g',x)
    except  StopIteration as e:                     #遇到此错误
        print('Generator return value:',e.value)    #打印返回值
        break


##3*********练习：杨辉三角
##def triangles():
##    L=[1]
##    while True:
##        yield L
##        newL = [1]     #首1
##        for x in range(1,len(L)):
##            newL.append(L[x-1]+L[x])
##        newL.append(1)      #尾1
##        L = newL[:]

#2
##def triangles():
##    b=[1]
##    temp=[1]
##    while True:
##        yield b   #定义成一个生成器，打印需要生成的数据
##        b.insert(0,0)
##        temp.append(0)
##        for i in range(0,len(b)):
##            b[i]=b[i]+temp[i]
##        temp=b[:]
##    return 'done'

#3
def triangles():
    L=[1]
    while True:
        yield L
        L=L[:]  #添加的解决方法
        i = -1
        while L[:i] != []:
            L[i] = L[i] + L[i-1]
            i = i - 1
        L.append(1)

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)          
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

##for t in triangles():
##    results.append(t)
##    print(results[0] , '-------' + str(n))
##    n = n + 1
##    if n == 10:
##        break
##print(results)#这个是你的结果，不是杨辉三角
##因为函数返回的实际上是内存中的地址，所以在下一次对变量的赋值之前，
##地址是不会改变的(添加这种不叫赋值，叫更新，a=b才叫赋值)，
##如果地址没有改变，这样的添加就会导致原来的元素也添加。
##解决的办法是在yield L后面加个L=L[:],这样就是新的地址，
##这样怎么修改都不会影响原来的。
