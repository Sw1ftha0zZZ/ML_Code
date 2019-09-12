import numpy as np 
import pandas as pd 
from pandas import Series,DataFrame


#丢弃指定轴上的项
obj=Series(np.arange(5),index=['a','b','c','d','e'])
new_obj=obj.drop('c')
print(new_obj)


#对于DataFrame可以删除任意轴上的索引值
data=DataFrame(np.arange(16).reshape((4,4)),index=['a','b','c','d'],columns=['1','2','3','4'])
print(data)
print(data.drop(['a','d']))

print(data.drop('2',axis=1))
print(data.drop(['2','4'],axis=1))



#Series索引的工作方式类似于numpy数组中的索引，只不过Series中的索引不只是整数

#利用标签的切片运算和普通的python切片运算不同
#利用标签的切片运算是包含末端的（inclusive）
#普通的python切片是不包含末端的（exclusive）



#对DataFrame进行索引是获取一个或者多个列
print(data)
print(data['2'],data[['2','3']])
#这种索引方式有几种特殊的情况，首先通过切片或布尔型数组选取行
print(data[:2])
print(data[data['3']>5])

#但是更多时候，如果要对DataFrame的行进行索引，我们使用ix函数

print(data.ix[2])
print(data.ix['b'])
print(data.ix[['b','c']])
print(data.ix[['b','c'],[0,1]])#第一个参数传行的，第二个参数传列的
print(data.ix[['b','c'],['4','2']])#传参数时既可以传整型又可以传字符型






#所以说所有的标签索引功能其实都可以在ix函数中实现






#算术运算和数据对齐

#pandas的一个重要功能是，它可以对不同索引的对象进行算术运算。
#在将对象相加时，如果存在不同的索引对，则结果的索引就是对该索引对的并集
#自动数据对齐使得在不重叠的索引处引入了NA值，缺失值在算术运算的过程中自动传播
#对于DataFrame，对齐操作会同时发生在行和列上


#在对不同索引对象进行算术运算时，你可能希望当中一个对象中某个轴标签在另一个对象中找不到时填充一个特殊值（比如0）
df1=DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
df2=DataFrame(np.arange(20).reshape(4,5),columns=list('abcde'))
print(df1,df2)

#使用add方法传入fill_value可以做到
print(df1.add(df2,fill_value=0))


#与此类似，在对Series或DataFrame进行重新索引时，也可以指定一个填充值

print(df1.reindex(columns=df2.columns,fill_value=0))

#DataFrame与Series之间的运算也是广播
#默认情况下会将Series的索引匹配到DataFrame的列，然后沿着行一直向下传播。


#如果某个索引值在DataFrame的列或Series的索引中找不到，则参与运算的两个对象就会被重新索引以形成并集


#如果你希望匹配行且在列上广播，则必须使用算术运算方法（add，sub等而不是+，-），并且要指定轴向




#排序和排名
#使用sort_index方法，它返回一个已排序的新对象

obj3=Series(np.arange(4),index=['d','a','c','b'])
print(obj3.sort_index())
#对于DataFrame也可以根据任意一个轴上的索引进行排序
#数据默认是按照升序的，也可以设置为降序
print(obj3.sort_index(ascending=False))

#排名


#处理确实数据--NAN
#利用dropna（）方法可以去除缺失数据
#默认丢失行，也可以设置丢失含na的列（axis=1）


#使用fillna可以做到填充缺失数据，将缺失值替换成指定的常数值
#通过一个字典调用fillna，可以实现对不同的列填充不同的值
#fillna也可以实现很多其他功能，比如填充series的中位数或平均数






#层次化索引
