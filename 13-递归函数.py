##1******
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#fact(n)=n!=fact(n-1)*n(除n=1时特殊)
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)  #表达式，故不是尾递归

#递归函数的使用事项：
#递归调用次数过多，会导致栈溢出：
#fact(1000)      #RecursionError: maximum recursion depth exceeded in comparison


'以下是废话'

#所以要：尾递归优化（循环可以看成特殊的尾递归函数）
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)
#fact(1000)      #结果同上：因为Python解释器也没有做尾递归优化……



##2******练习
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)        #1个时整体移动
    else:    
        move(n-1,a,c,b)         #a柱n-1个盘子移动到b柱
        move(1,a,b,c)
        move(n-1,b,a,c)
##def move(n,a,b,c):
##    if n == 1:
##        print(a,'-->',c)        #1个时整体移动
##        return  
##    move(n-1,a,c,b)             #a柱n-1个盘子移动到b柱
##    move(1,a,b,c)
##    move(n-1,b,a,c)
#### def move(n,a,b,c):
####    if n==1:
####        print (a,'--->',c) #递延算法的特点,要设一个停止位
####    else:
####        move(n-1,a,c,b) #把n-1个移动到B柱
####        move(1,a,b,c)   #把最底下的移动到C柱
####        move(n-1,b,a,c)  #余下的移动到C柱               
    
move(3,'A','B','C')
