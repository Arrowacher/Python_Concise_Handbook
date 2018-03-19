##直接作用于for循环的数据类型：
#1.集合数据类型：如list，tuple，dict，set，str等
#2.generator：生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable对象


##1********
#可以使用isinstance()判断一个对象是否是Iterable的对象：
from collections import Iterable
isinstance([],Iterable)                         #list
isinstance({},Iterable)                         #tuple
isinstance('abc',Iterable)                      #str
isinstance((x for x in range(10)),Iterable)     #generator
isinstance(100,Iterable)                        #-》False

#True,False在Shell中

##2*********
#instance()判断是否是Iterator
from collections import Iterator
isinstance((x for x in range(10)),Iterator)     #T
isinstance([],Iterator)                         #F
isinstance({},Iterator)                         #F
isinstance('abc',Iterator)                      #F
#generator是Iterator对象，但list、dict、str是Iterable，却不是Iterator

#可作用于for循环      #可被next不断调用并返回下一个值
#Iterable对象      >  #迭代器：Iterator                  >#生成器：generator


##3*****Iterable—>Iterator：iter()
isinstance(iter([]),Iterator)
isinstance(iter('abc'),Iterator)

#Iterator表示一个惰性序列，只有在需要下一个数据时才会计算


##4***********
#for循环本质上就是通过不断调用next()函数实现的：
for x in [1,2,3,4,5]:
    pass
#完全等价于：
it = iter([1,2,3,4,5])      #首先获得Iterator对象
#循环：
while True:
    try:
        #获得下一个值
        x = next(it)
    except StopIteration:
        #退出循环
        break

#可迭代对象中的元素都是存放在内存中，都是有限的，
#而迭代器的对象本质上可以不包含元素，而是通过next()来不断获取。



#question:
#为何？
##o=triangles()
##next(o)
##next(o)
##这种值会不断迭代，
##而
##next(triangles())
##next(triangles())
##却一直返回[1]?
#o=triangles() next(o) next(o)是对同一个对象进行迭代，
##next(triangles()) next(triangles())两次next是对不同对象进行迭代，
##每一次triangles()返回的都是一个新的对象
