#python的函数灵活度非常大，除了正常定义的必选参数
#还可以有默认参数、可变参数和关键字参数，使得函数定义出来的接口，
#不但能处理复杂的参数，还可以简化调用者的代码。

##1******位置参数
def power(x):
    return x*x
#power(x)函数，参数x就是一个位置参数，必须传入一个参数x：
print(power(5))

#升级power函数：
def power(x,n):
    s=1
    while n > 0:
        s = s*x
        n = n-1
    return s
print(power(2,4))



##2******默认参数
def power(x,n=2):
    s=1
    while n > 0:
        s = s*x
        n = n-1
    return s
print(power(5))
print(power(5,3))
#
def enroll(name,gender):            #enroll(v.)入学，加入 #gender n.性别
    print('name:',name)
    print('gender:',gender)

enroll('Sarah','F')

#^
def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
enroll('Tom','M')           #大多数学生
enroll('刘炫','男',22,'Zhangjiajie')   #特殊学生
enroll('刘小强','男',city = '忻州')

#!!!#默认参数的一个大坑：
def add_end(L=[]):      #默认参数L是一个变量！L指向对象[]
    L.append('end')     #每次调用函数都会改变L的内容，给L的对象加个'end'
    return L
print(add_end())
print(add_end())
#总结：默认参数的对象要牢记：必须指向不变对象！

#^
def add_end(L=None):    #这次默认为None(None,str等为不变对象，一旦创建，对象内部数据不能修改)
    if L is None:
        L = []          #实现None转换成[]
    L.append('END')
    return L
print(add_end())
print(add_end())



##3*******可变参数：参数个数可变
#a^2+b^2+c^2+……
def calc(numbers):      #calculate v.计算
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,3]))    #但是调用的时候需要先提供list或tuple
#^利用可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#仅仅相差一个*，可以传入任意个参数，包括0个参数：
print(calc(1,2,3))
print(calc())
#^若已经有一个tuple/list形式的数据，应用到可变参数的函数中：
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))        #繁琐的应用
print(calc(*nums))              #Python允许加*号，把list或tuple的元素变成可变参数传进去
#所以*的作用可能是可变参数数据与list/tuple数据之间的切换


#4********关键字参数：0个过任意个有参数名的参数->dict
def person(name,age,**kw):          #kw, 简写key words
    print('name:',name,'age:',age,'other:',kw)
    #必选参数：name，age||关键字参数：kw
person('Michael',30)                            #只有必选参数的调用
person('Bob',35,city='Beijing')                 #
person('Adam',45,gender='M',job='Engineer')     #任意个数关键字参数的调用

#总结：关键字参数可以扩展函数的功能：例如在person函数中能保证接收到name和age的参数，
#      但是如果有更多参数数据，也能接收到。（注册用的选填项与必填项）

#已经有一个dict：
extra = {'city':'Beijing','job':'Engineer'}
person('Jack',36,city=extra['city'],job=extra['job'])   #复杂的调用
person('Jack',36,**extra)


##5*************命名关键字参数
#检查person()函数中是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw:
        pass        #假如有就xxxx
    if 'job' in kw:
        pass        #假如有就xxxx（这里跳过）
    print('name:',name,'age:',age,'other:',kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
#仍然可以传入不受限制的关键字参数
#限制关键字参数：用命名关键字参数
def person(name, age,*, city, job):     #*后面视为命名关键字参数,只接收city和job作为关键字参数
    print(name, age, city, job)
person('Jack',36,city='Beijing',job='Engineer')
#必须写上city和job的参数名，因为person只接收2个位置参数
#上句限制了关键字参数的名，不支持其他关键字参数，会报错


def person(name, age,*, city='Beijing', job):
     print(name, age, city, job)

person('Jack',24,job='Engineer')        #命名关键字参数具有默认值时，可不传入

#坑：
def personX(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass        #无pass报错



##6*******参数组合：必选，默认，可变，命名关键字和关键字（定义顺序）
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

#用一个tuple和dict，你也可以调用上述函数：

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#a= 1 b= 2 c= 3 args= (4,) kw= {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}


##******练习
def product(*args):
    s = 1
    for n in args:
        s = s * n
    return s
#test:
print(product())
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!0')
elif product(5, 6) != 30:
    print('测试失败!1')
elif product(5, 6, 7) != 210:
    print('测试失败!2')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!3')
else:
    try:                            #规避错误:若发生TypeError错误，执行缩进
        product()                   
    except TypeError:
        print('测试失败!')
    else:                           #若没有触发错误，执行缩进
        print('测试成功')  
