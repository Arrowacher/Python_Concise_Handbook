##1*****函数本身可以赋给变量
f = abs
print(f)
print(f(-10))       #变量f已经指向了函数本身：调用f()和调用abs()相同


##2*****函数名也是变量
#abs可以看成变量：它指向一个可以计算绝对值的函数
#abs = 10
abs(-10)
##Traceback (most recent call last):
##TypeError: 'int' object is not callable
#因为abs已经不指向求绝对值函数，而是指向整数10

#注：由于abs函数实际上是定义在import builtins模块中的，所以要让
#修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。


##3****函数中用函数就是高阶函数
def add(x,y,f):
    return f(x) + f(y)

print(add(-5,6,abs))
