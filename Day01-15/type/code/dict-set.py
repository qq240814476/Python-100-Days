# dict(map)
# 注意：返回None的时候Python的交互式命令行不显示结果。

a = {'a': 1, 'b': 2}
print('v' in a)

# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

a.get('Thomas')
a.get('Thomas', -1)
# -1

# 删除元素方法
a.pop('a')

# set 同js的set  无序无重复的list
# 可以做交集，去重运算
s = set([1, 1, 2, 2, 3, 3])
print(s)
# {1,2,3}

# 函数参数要指向   不变对象 ！！！

# 可变参数  * + params
def aaaa(*bbb):
  for i in bbb:
    print(i)

# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。