#在我们传入函数时，有些时候，不需要显示地定义函数，直接传入匿名函数更方便。
#python有限支持匿名函数
#例：计算f(x)=x*x时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
s = list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
print(s)
#匿名函数lambda x:x*x实际是：
def f(x):
    return x*x

##匿名函数可以赋值给变量
f = lambda x:x*x
print(f)
print(f(5))


##匿名函数可作为返回值返回
def build(x,y):
    return lambda:x*x +y*y


#练习：请用匿名函数改造下面的代码：
def is_odd(n):
    return n%2 ==1
L=list(filter(is_odd,range(1,20)))

print(L)
#
L1=list(filter(lambda x:x%2==1,range(1,20)))
print(L1)
