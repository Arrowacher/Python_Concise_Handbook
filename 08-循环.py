#1*******for x in循环:依次迭代list或tuple的元素到变量x
names = ['A','B','C']
for x in names:         #我第一次漏掉了:
    print(x)            #每一次迭代都会执行print
##
#2******累加1-10
sum = 0
num = [1,2,3,4,5,6,7,8,9,10]    #注意到列出list或tuple对于多数字时的情况太麻烦!(见3)
for x in num:
    sum = sum +x        #循环此句
print(sum)              #循环结束后的结果
##
#3*******使用range()生成整数序列
#range(5)生成0-4的整数
print(range(5))   #显示range（0,5）
print(range(0,5))   #显示同上，说明 range(5)就是range(0,5)
print(list(range(5)))   #显示成list形式->[0,1,2,3,4]

#累加1-100
sum = 0
Listone=list(range(101))    
for y in Listone:   #我第二次忘记:
    sum = sum + y
print(sum)
    #这样少一步
sum1 = 0    
for x in list(range(101)):   #我第二次忘记:
    sum1 = sum1 + x
print(sum1)
        #更简单的做法
sum2 = 0
for z in range(101):    #直接从整数序列中迭代
    sum2 = sum2 + z
print(sum2)




###########
#4**********while循环，不满足条件时结束。
n=99
sum = 0
while n>0:              #忘记:第三次
    sum = sum + n
    n = n-2             #直到n=-1，<0时结束循环
print(sum)

#练习：
L = ['Bart', 'Lisa', 'Adam']
for x in L:             #选择for in
    print('Hello,%s!'%x)


##
#5********循环中的break：提前结束循环
#例如#
##n=1
##while n < 101:          #忘记第四次
##    print(n)
##    n=n+1 
##print('end')                打印1-100
n=1
while n <101:
    print(n)
    n=n+1
    if n>10:
        break
print('end')


##
#6**********循环中的continue：跳过这次循环，开始下一次。
n=0
while n<10:             #忘记第五次
    n = n+1
    if n % 2 == 0:      # 如果n是偶数，执行continue语句
        continue
    print(n)

####总结####
#####如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。
#这时可以用Ctrl+C退出程序，或者强制结束Python进程。
#####要特别注意，不要滥用break和continue语句。
#break和continue会造成代码执行逻辑分叉过多，容易出错。
#大多数循环并不需要用到break和continue语句
#上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

