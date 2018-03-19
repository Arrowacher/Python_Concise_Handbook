#把函数作为结果返回
##1--通常情况下的求和函数：
def calc_sum(*args):
    ax=0
    for n in args:
        ax = ax + n
    return ax               #立刻求和
#不立刻求和的情况：返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax=ax+n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
print(f)     #x
print(f())   #

#p.s.:调用lazy_sum()时，每次调用都会返回一个新的函数：
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1 == f2)     #False


##2*****闭包：函数的内部函数包含了参数
def count():
    fs = []
    for i in range(1,4):
        def f():
            print('qi=',i)
            return i*i
        print('hi=',i)
        fs.append(f)   #更新、添加f的地址
    return fs
f1,f2,f3 = count()     #这个等式的含义应该是：把count()结果的前三分配
print(f1(),f2(),f3())
#f1()  :9
#f2()  :9
#f3()  :9       #原因：返回的fs中有函数f，它并非立刻执行，三个函数都返回后i为3

#！！！#返回闭包时：返回函数不要引用任何循环变量，或者后续会发生变化的变量（如上）


##3****闭包引用循环变量的方法：再创建一个函数绑定循环变量当前的值
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) #f(i)立即执行，i值直接传入f()
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())


##4****闭包返回计数器函数，每次调用它返回递增整数
#简单的方法：
##def createCounter():
##    n=[0]
##    def counter():
##        n[0]=n[0]+1
##        return n[0]
##    return counter
#
def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
