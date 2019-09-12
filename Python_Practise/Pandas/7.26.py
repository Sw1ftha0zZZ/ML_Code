#pandas是基于numpy构建的，提供更简单的高级数据结构

from pandas import Series,DataFrame
import pandas as pd

#pandas的两个主要数据结构：Series和DataFrame

#Series是一种类似于一维数组的对象，它由一组数据（numpy类型）和一组与之相关的数据标签（索引）构成
#Series的字符串表现形式为索引在左边，值在右边，由于我们没有为数据指定索引，于是会自动创建一个从0到n-1的索引
#可以通过Series的values和index属性获得其数组的表现形式和索引对象
obj=Series([4,7,8,2])
print(obj)
print(obj.values)
print(obj.index)

#当然也可以按如下方式指定索引
obj1=Series([4,7,8,2],index=['a','c','b','d'])
print(obj1)
print(obj1.index)

#与numpy数组相比，你可以通过索引的方法选取Series中的单个或一组值
print(obj1['a'])
print(obj1[['a','b','d']])

#numpy数组运算（如根据布尔型数组进行过滤，标量乘法，应用数学函数等）都会保留索引和值之间的链接。



#如果数据被放在一个python字典中，也可以直接通过这个字典来创建Series
sdata={'Olly':231,'Bill':2131,"Billy":212121,"Jon":786}
obj2=Series(sdata)
states={'Olly',"Billy","Alice","Bill"}
obj3=Series(sdata,index=states)
print(obj3)
#在这个例子中，与索引匹配的会被找出来并放在相应位置上，找不到的结果是NAN（非数字），在pandas中它表示缺失或NA值
#Series的一个重要功能是：它在算术运算中会自动对齐不同索引的数据
print(obj2+obj3)



#Series对象及其索引都有一个name属性，这个属性和pandas的其他关键功能关系非常密切
obj3.name='population'
obj3.index.name='state'
print(obj3)


#Series的索引可以通过赋值的方式就地修改
obj3.index=['olly','billy','alice','bill']
print(obj3)