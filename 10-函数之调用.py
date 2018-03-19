##1******调用函数需要知道函数的名称和参数
##http://docs.python.org/3/library/functions.html#abs查看官网文档
##或者help()查看：help(abs)
#取绝对值abs()
abs(-5)
#取最大值
max(1,5)
#把其他数据类型转换成整数int()
int('123')
int(12.34)
float(12.34)    #浮点数
str(1.23)       #'1.23'
str(100)
bool(1)         #True
bool('')        #False


##函数的赋名调用：
a = abs         #变量a指向abs函数
a(-1)           #a也能调用abs函数了
print(a(-1))


