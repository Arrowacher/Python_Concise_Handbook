print('%02d-%10d' % (3,1))
print('%.3f'%3.1415926)

print('\n\n\n\n')

s1 = float(72)
s2 = float(85)
r = (s2-s1)/s1*100
print(s1,s2,r)
print('小明成绩提升了%.1f%%' % r)


print('\n\n\n\n')


print("这是计算成绩提高百分比的简单程序，请按照提示输入对应信息")#开头提示语，让程序更具互动性！
name=input('请输入你的名字:')
s1=float(input('%s,请输入你去年的成绩:'%name))
s2=float(input('%s,请输入你今年的成绩:'%name))
r=(s2-s1)/s1*100
print('%s,你的去年成绩是%f，今年成绩是%f，\n成绩比去年提高了：%.2f%%'%(name,s1,s2,r))


##18.3.5补充：
##自python2.6开始，新增了一种格式化字符串的函数str.format()，此函数可以快速处理各种字符串。
##语法
##它通过{}和:来代替%。
#通过位置
print('{0},{1}'.format('chuhao',20))

print('{},{}'.format('chuhao',20))

print('{1},{0},{1}'.format('chuhao',20))

#通过关键字参数
print('{name},{age}'.format(age=18,name='chuhao'))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'This guy is {self.name},is {self.age} old'.format(self=self)

print(str(Person('chuhao',18)))

#通过映射 list
a_list = ['chuhao',20,'china']
print('my name is {0[0]},from {0[2]},age is {0[1]}'.format(a_list))
#my name is chuhao,from china,age is 20

#通过映射 dict
b_dict = {'name':'chuhao','age':20,'province':'shanxi'}
print('my name is {name}, age is {age},from {province}'.format(**b_dict))
#my name is chuhao, age is 20,from shanxi

#填充与对齐
print('{:>8}'.format('189'))
#     189
print('{:0>8}'.format('189'))
#00000189
print('{:a>8}'.format('189'))
#aaaaa189

#精度与类型f
#保留两位小数
print('{:.2f}'.format(321.33345))
#321.33

#用来做金额的千位分隔符
print('{:,}'.format(1234567890))
#1,234,567,890

#其他类型 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。

print('{:b}'.format(18)) #二进制 10010
print('{:d}'.format(18)) #十进制 18
print('{:o}'.format(18)) #八进制 22
print('{:x}'.format(18)) #十六进制12
