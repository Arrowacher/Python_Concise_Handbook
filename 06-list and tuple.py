print('可修改的有序列表list')
ehero=['羽翼','爆热','水泡','黏土','闪电']
print(ehero)
ehero.append('野蛮')
print(ehero)
ehero.insert(5,'新宇')
print(ehero)
ehero.pop()
print(ehero)
ehero.pop(1)    #pop(-1)就是指最后位置的元素，以此类推
print(ehero)
ehero[4]='爆热'
print(ehero)
newspace=['蜂鸟','黑豹','青苔']
ehero.insert(0,newspace)
print(ehero)
print(ehero[0][2])

print('不可修改的有序列表tuple')
baoyu=('青玉','红玉','琥珀','翡翠','紫晶','黄玉','蓝骷')
print(baoyu)
print('tuple定义中需要注意的地方：')
t1=(1,2)
print('t1=',t1)
t2=()
print('t2=',t2)
t3=(1)
print('t3=',t3,'\nt3是错的，t3=(1)产生计算括号内容的歧义,正确是t4')
t4=(1,)
print('t4=',t4)


print('"可变"的tuple,tuple的指向不变论！')
t=('a','b',['A','B'])
print('t=',t)
t[2][0]='X'
t[2][1]='Y'
print('t=',t)
print('tuple的指向的list没变，还是那个list，但是list的指向变了')

