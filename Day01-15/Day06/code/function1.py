"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) / factorial(3))
print('''aaa
bbb
ccc''')

# r不转义
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, \n'
s4 = r'''Hello,
Lisa!'''
print(s3)
print('growth rate: %d %%' % 7)
s1 = 72
s2 = 85
r = (s2-s1) / s1
print('%.1f' % r)
