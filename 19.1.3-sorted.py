##排序（冒泡排序，快速排序）：核心是比较2个元素的大小。

##1*****sorted()-list-默认排序小到大
s = sorted([36,5,-12,9,-21])
print(s)

##2****sorted()-高阶函数：接收一个key函数自定义排序
s1 = sorted([36,5,-12,9,-21],key=abs)   #绝对值小大排序
print(s1)
#p.s. key指定的函数将作用于list每个元素

#
s2 = sorted(['bob','about','Zoo','Credit'])
print(s2)
#默认是按照ASCII的大小：‘Z'<'a'

#忽略大小写排序
s3=sorted(['bob','about','Zoo','Credit'],key=str.lower)
print(s3)
#反向排序：传入reverse=True
s4=sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print(s4)



##3*****练习
#用一组tuple表示学生的名字和成绩
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#用sorted()对上述列表分别按名字排序
def by_name(t):
    return t[0]
L2 = sorted(L,key=by_name)
#print('直接排：',sorted(L))
print(L2)
#再按成绩高低排序：
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)

#或者
def by_score1(t):
    return t[1]
L22 = sorted(L, key=by_score1,reverse=True)
print(L22)
