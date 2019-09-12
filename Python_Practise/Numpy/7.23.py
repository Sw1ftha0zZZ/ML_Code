#19.7.23
from __future__ import print_function
a=[1,2,3]
b=a
#python是按引用传递的，不会发生任何复制
print(a is b)
c=list(a)
#list()函数始终会创建新的列表
print(c)
print(c is a)#用于比较是否是同一个对象
print(c==a)#用于比较内容是否相同

#列表[],数组，字典等大部分用户自定义的类都是可变的
#元组(),字符串是不可变的，不可变的意思是不能修改原内存
#块中的数据，即使修改操作成功了，也是创建了一个新对象
#并将其引用赋值给原变量而已。



cval=1+2j
print(cval*(1-2j))
print(3//2)
print(3/float(2))

c="""
helloworl
d
"""
print(c)#使用三引号可以换行

sum=0
seq=[1,2,3,4]
for i in range(len(seq)):
    sum=sum+seq[i]
print (sum)