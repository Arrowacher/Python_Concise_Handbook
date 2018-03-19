#
def now():
    print('2018')
f=now
now()
f()
#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)

##假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望
##修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”

##1****装饰器decorator本身就是一个返回函数的高阶函数
#打印日志的decorator
def log(func):                                #接收一个函数
    def wrapper(*args,**kw):                 #返回函数执行：
        print('call  %s()'%func.__name__)                    #打印日志
        return func(*args,**kw)                              #运行接收函数
    return wrapper                            #返回一个函数
#*args  用来[解包list]将参数打包成tuple给函数体调用
#**kw   打包关键字参数成dict给函数体调用
#wrapper()函数的参数定义是(*args, **kw)，使它可以接受任意参数的调用

#log是一个decorator，接收一个函数，返回一个函数。
#需要借助@语法，把装饰器置于函数的定义处：
@log                         
def now():
    print('2018-2')         #装饰标记
#@log相当于执行了语句：now = log(now)       #这样now指向了新函数，即log()函数中返回的wrapper()函数
now()
#call now()
#2018-2
print(now.__name__)

##2******果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
#自定义log文本：
def log(text):                                        #1*text
    def decorator(func):                              #2*func
        def wrapper(*args, **kw):                     #3*
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#用法：
@log('execute')             #now = log('execute')(now)
def now():
    print('2018-2-27')

now()
#！！！#最后一步
print(now.__name__)
#经过装饰器，now.__name__变成了wrapper
#因为返回的那个wrapper()函数名字就是'wrapper'，
#所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。
#Python内置的functools.wraps就是干这个事的

##3***完整的decorator
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
#带参数的decorator则是：
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


##4****练习：作用于任何函数上，并打印该函数的执行时间
import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start_time=time.time()            #获取开始时间
        func = fn(*args,**kw)             #运行函数，把计算结果给func
        end_time=time.time()              #获取结束时间
        runtime=end_time - start_time        
        print('%s executed in %s ms' %(fn.__name__,runtime))
        return func                       #返回计算结果
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    print(x+y)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    print(x*y*z)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')



##4******练习2：编写一个decorator，在函数前后打印出xx，支持有无参数
import functools

def log(text):
    if isinstance(text,str):        
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call',text)
                fn = func(*args, **kw)
                print('end call',text)
                return fn
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call')
            fn = text(*args, **kw)
            print('end call')
            return fn
        return wrapper
@log
def f1():
    print('%s()无参数'%f1.__name__)
@log('我是参数')
def f2():
    print('%s()有参数'%f2.__name__)
f1()
f2()
        
