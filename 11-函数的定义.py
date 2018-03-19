##1******def语句:def name(参数):
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-7))
#用return随时返回函数结果
#函数执行完毕也没有return语句时，自动return None

##2*******pass语句
#如果想定义一个什么也不做的函数
def nop():
    pass
#可以用来作占位符，比如还没想好怎么写函数的代码，就可以先放一个pass，让代码运行起来
#e.g.
#if age>=18:
#    pass            #缺少pass，代码运行会有语法错误



##3*******参数检查
#调用函数时，若参数个数不对：TypeError
#若参数类型不对,python解释器无法帮助我们检查：
##>>> my_abs('A')
##TypeError: unorderable types: str() >= int()
##>>> abs('A')
##TypeError: bad operand type for abs(): 'str'
def new_abs(x):
    if not isinstance(x,(int,float)):       #若x不是int或float类型
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


##4*******返回多个值
#例如游戏中常需要从一个点移动到另一个点，需要给出坐标，位移和角度，就能计算出新的坐标
import math         #表示导入math包，并允许后续代码引用math包里的sin、cos等函数

def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny
a,b = move(100,100,60,math.pi/6)
print(a,b)  #151.…  70.0  用多个变量接受一个tuple
#but
r = move(100,100,60,math.pi/6)
print(r)    #(151.…, 70.0)说明返回的是一个tuple，但是返回tuple可以省略括号
#总结：函数可以同时返回多个值，其实就是一个tuple


##5*****练习
import math
def quadratic(a,b,c):
    lll=math.sqrt(b**2-4*a*c)
    x1 = (-b+lll)/(2*a)
    x2 = (-b-lll)/(2*a)
    return x1,x2
#测试：
print('quadratic(2,3,1) =',quadratic(2,3,1))
print('quadratic(1,3,-4) =',quadratic(1,3,-4))
if quadratic(2,3,1) != (-0.5,-1.0):
    print('测试失败')
elif quadratic(1,3,-4) != (1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')
    
