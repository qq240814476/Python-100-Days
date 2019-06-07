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