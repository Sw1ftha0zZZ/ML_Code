import pandas as pd 
import numpy as np 
from pandas import Series,DataFrame

df=pd.read_csv('test.csv')
print(df)

#也可以用pd.read_table(),不过要指定分隔符为‘，’
df2=pd.read_table('test.csv',sep=',')
print(df2)


#并不是所有文件都有标题行，读入没有标题行的文件
#可以让pandas为其分配默认的列名，也可以自己取列名
#pd.read_csv('test2.csv',header=None)这个是让pandas为其分配默认的列名
#pd.read_csv('test2.csv',names=['a','b','c','d','message'])这个是指定好的



#如果希望指定某一列为索引
#pd.read_csv('test2.csv',names=['a','b','c','d','message'],index_col='message')
#这样可以做到指定message列为索引




#如果希望将多个列作为层次化索引，只需要传入由列编号或列名组成的列表即可
#pd.read_csv('test2.csv',index_col=['message','a'])




#如果表格不是用固定的分隔符去分割字段的，可以采用正则表达式去匹配字符串
#pd.read_table('test.txt',sep='\s+')这样可以做到将多个空格作为分隔符


#如果文件中有几行不是表格，是其他不想要的东西，用skiprows可以做到跳过
#pd.read_csv('test.csv',skiprows=[2,4,5])


#在书上有read_csv()的参数




#逐块读取文本文件
#如果只想读几行，通过nrows可以指定
#pd.read_csv('test.csv',nrows=2)

#要逐块读取文件，需要设置chunksize（行数）,然后用chunker去迭代
#chunker=pd.read_csv('test.csv',chunksize=1000)
#tot=Series([])
#for piece in chunker
#   tot=tot.add(piece['key'].value_counts(),fill_value=0)
#tot=tot.sort_values(ascending=False)



#写出到文件用to_csv('')




#Json数据是一种比表格形式灵活得多的数据格式
#Json非常接近于有效的python代码，
#json.loads()可以将json字符串转换为python形式
#json.dumps()将python对象转化为json格式



#二进制数据格式
#实现数据的二进制格式存储的最简单方法是使用python内置的pickle序列化
#为了使用方便，pandas对象都有一个用于将数据以pickle形式保存到磁盘上的save方法


#HDF5格式
#对于那些非常大的无法直接放入内存的数据集，HDF5就是不错的选择，因为它可以实现分块读写
#HDF5适合用作一次写多次读的数据集




#数据转换
#DataFrame中经常会出现重复行，假设data是一个df
#data.drop_duplicates()返回一个移除了重复行的df
#这个方法会默认判断所有列是否有重复
#也可以指定对部分列进行重复项判断
#data.drop_duplicates(['key'])这就是对key列查重
#这个方法会默认保留第一个
#data.drop_duplicates(['key],take_last=True)这样是保留最后一个



#替换值

#replace（a,b）方法可以做到把a换成b，fillna是replace的一种特殊情况