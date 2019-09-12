from pandas import Series,DataFrame
import pandas as pd
import numpy as np

#DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型
#DataFrame既有行索引又有列索引，它可以被看做是由series组成的字典（共用同一个索引）



#构建DataFrame的方法有很多，最常用的一种是直接传入一个由等长列表或Numpy数组构成的字典
data={'state':['Ohion','ohu','sa','ta','us'],
      'year':[2000,1221,212,1212,5656],
      'pp':[1.3,12,1.2,1,1]}
frame=DataFrame(data)
print(frame)
#结果DataFrame会自动加上索引（跟Series一样），且全部列会被有序排列



#如果指定了列序列，则DataFrame中的列会按照指定顺序进行排列
frame2=DataFrame(data,columns=['year','pp','state'])
print(frame2)



#跟Series一样，如果传入的列在数据中找不到，则会产生Na值
frame3=DataFrame(data,columns=['year','pp','state','debt'],index=['one','two','three','four','five'])
print(frame3)
print(frame3.columns)


#可以通过如下两种方式对列进行访问
print(frame3.year)
print(frame3['pp'])
#此时便将DataFrame中的列获取为一个Series，返回的Series与原有的DataFrame具有相同的索引



#行也可以通过位置或者名称的方式进行获取，比如用索引字段ix
print(frame3.ix['three'])



#列也可以通过赋值的方式进行修改
frame3['debt']=21
print(frame3)

frame3['debt']=np.arange(5)
print(frame3)
#将列表或数组赋值给某个列，其长度必须与DataFrame的长度相匹配

#如果赋值的是一个Series，就会精确匹配到DataFrame的索引，所有的空位都将补上缺失值
val=Series([1.2,1.3,1.4],index=['two','three','five'])
frame3['debt']=val
print(frame3)


#为不存在的列赋值会创建出一个新列。关键字del用于删除列
frame3['nu']=frame3.state=='Ohion'
print(frame3)



#关键字del用于删除列
del frame3['nu']
print(frame3.columns)



#另一种常见的数据形式是嵌套字典（也就是字典的字典）
pop={'Na':{2000:2.1,3212:2.4},'Oh':{2000:1.2,2001:2.3,3212:2.33}}
#如果将他传给DataFrame，它就会被解释为：外层字典的键作为列，内层键作为行索引
frame4=DataFrame(pop)
print(frame4)
print(frame4.T)


#如果设置了DataFrame的index和columns的name属性，则这些信息也会被显示出来
frame4.index.name='year'
frame4.columns.name='state'
print(frame4)

#跟Series一样，values属性也会以二维ndarray的形式返回DataFrame中的数据
print(frame4.values)



#pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）
obj=Series(range(3),index=['a','b','c'])
index=obj.index
print(index)
#index[1]='d'是错的
#index对象是不可修改的immutable，因此用户不可以对其进行修改
#不可修改性非常重要，因为这样才可以使Index对象在多个数据结构之间安全共享。




#重新索引




#pandas里面的reindex，调用reindex会根据新索引进行重新排序，如果某个索引值当前不存在，就引入NaN
obj=Series([1.1,2.1,3.1,4.1],index=['d','c','b','a'])
obj2=obj.reindex(['a','b','c','d','e'])
print(obj2)
obj2=obj.reindex(['a','b','c','d','e'],fill_value=0)
print(obj2)



#对于时间序列这样的有序数据，重新索引时可能需要做一些插值处理，method选项可以达到这个目的，method可以实现插值填充方法
#ffill可以实现前向值填充
obj3=Series(['blue','purple','yellow'],index=[0,2,4])
print(obj3)
print(obj3.reindex(range(6),method='ffill'))
print(obj3.reindex(range(6),method='bfill'))



obj4=DataFrame(np.arange(9).reshape((3,3)),index=['a','d','c'],columns=['Ohio','Texas','California'])
print(obj4)
print(obj4.reindex(['a','b','c','d']))
states=['Texas','Utah','Ohio']
#使用columns可以重新索引列
print(obj4.reindex(columns=states))