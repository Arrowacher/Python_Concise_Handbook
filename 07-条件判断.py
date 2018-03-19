#if xxx:\nelse:xxx
age=3
if age >= 60:
    print('old man')
elif age >=18:
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('kid')

print('练习：')
'''
bmi = float(weight/height**2)
print('bmi=',bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi >28 and bmi <=32:
    print('肥胖')
elif bmi >25 and bmi <=28:
    print('过重')
elif bmi >=18.5 and bmi <=25:
    print('正常')
else:print('过轻')       残次品
'''           

h=float(input('please enter your height(m):'))
w=float(input('please enter your weight(kg):'))
bmi=w/h**2
print('bmi = %.1f'%bmi) #不用加逗号！！！
if bmi > 32:
    print('严重肥胖')
elif 28 < bmi <= 32:
    print('肥胖')
elif 25 < bmi <=28:
    print('过重')
elif 18.5 <= bmi <=25:
    print('正常')
else:print('过轻') 
