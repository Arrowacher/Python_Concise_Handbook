#1******python的内置字典 ：dict，其他语言中也成为map，储存方式：key-value
#极快的查找，key找value
d =  {'Michael':95,'Bob':80,'Tom':75}   #使用{}大括号
print(d['Michael'])

#使用key放入            ##使用key相关的方法时是[]中括号哦！##
d['Marry'] = 60
print(d)
d['test'] =  'dog'

d['Marry'] = 99     #值会覆盖
print(d)
#用key获取value
print('Marry的成绩是',d['Marry'])

##获取时碰到的问题：判断 key的存在与否##
print('Tom' in d)       #打印‘True’
print('Tom')            #打印‘Tom’
print('tom' in d)       #打印‘False’

#获取value的另一个方法（不使用d['']）
##get()##key如果不存在的话不会报错，而是会默认返回None,也可以指定返回值
print(d.get('Jay'))     #返回None（交互环境不显示None）
print(d.get('Jay',-1))  #返回-1


#dict中的key的删除:pop()
d.pop('Michael')
print(d)
##？->X##d.pop()    无法删除任何key，list中这样可以删除最后一个

#P.S.:list集合不能作为key，因为list是可变的。



#2**********set也是key的集合，但不储存value。需要提供list传入数据。
s = set([1,2,2,3])
print(s)    #{1,2,3}自动过滤重复！显示顺序不代表set有序

#add(key)
s.add(5)
s.add('single dog')
print(s)
#remove(key)
s.remove('single dog')
print(s)

###set()用法：数学意义上的无序、无重复的集合，因此两个set可以做数学意义上的交、并集操作。
s1 = set([1,2,3])
s2 = set([2,3,4])
print('交集',s1&s2)
print('并集',s1|s2)



#3*******不可变对象str，与可变对象list
a = ['c','b','a']   #可变list
a.sort()
print(a)    #['a','b','c']结果变了


a = 'abc'           #不可变str
b = a.replace('a','A')
print(a)            #'abc'未变
print(b)            #'Abc':a是变量，'abc'才是字符串对象，b指向新的字符串。


##test：tuple
x = set((1,2,3))
print(x)
y = set((1,[2,3]))
print(y)
#总结：tuple中x可行，附带list元素的不可行
