#python內建filter()用于过滤序列
#与map()区别，filter(f,[])根据返回值是True还是False决定保留还是丢弃该元素

##1*****删偶保奇
def is_odd(n):
    return n%2 ==1      #返回余值为1的（奇数）
print(list(filter(is_odd,[1,2,4,5,6,9,10,15]))) #filter()
#python3起，filter函数返回的对象从列表改为Iterator（迭代器）
#迭代器：惰性序列啊，在需要下一个值时才计算出来
#而生成器()有自动生成功能，一边循环一边计算{列表生成式[]}


##2****删除序列的空字符
def not_empty(s):
    return s and s.strip()  #去除前后空格
#这句的作用是让中部分有字的返回1，前后空格返回0
print(list(filter(not_empty,['A','','B',None,'C','  '])))
#结果：['A','B','C']


##3****求素数：埃氏筛法
#构造从3开始的奇数序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n #注意与print的区别
#定义一个筛选函数：
def _not_divisible(n):
    return lambda x:x % n > 0
#定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()        #初始序列
    while True:
        n = next(it)        #返回序列第一个素数
        yield n
        it = filter(_not_divisible(n),it)   #构造新序列

#打印100以内的素数：
for n in primes():
    if n<100:
        print(n)
    else:
        break

##4*****练习：filter()筛选回数：12321、909
def is_palindrome(n):
    s = str(n)      #num->str
    s1 = s[::-1]    #前面加了一个：从哪取：-（右取）几位取
    return s == s1
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
