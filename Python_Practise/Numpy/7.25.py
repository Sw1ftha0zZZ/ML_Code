#19.7.25
#数组切片是原始数组的视图，对视图的任何修改都会直接反映到原数组上
import numpy as np
arr=np.arange(10)
print (arr)
print(arr[5:8])
arr[5:8]=12
print (arr)
#numpy不复制数组，这样更有利于大数据处理


#获取或者设置数组子集的一个办法是通过整数数组使用花式索引



#如果想得到ndarray的一份副本，而非视图，就要做显式的
#复制操作 arr[5:8].copy()
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
old_values=arr2[0].copy()
arr2[0]=100
print (arr2)
arr2[0]=old_values
print (arr2)



#数组转置和轴对换
arr3=np.arange(15).reshape((3,5))
print(arr3,arr3.T)
#利用np.dot可以计算矩阵内积
print(np.dot(arr3.T,arr3))

#对于高维数组
print(np.arange(16).reshape(2,2,4))
print (np.arange(16).reshape(2,2,4).transpose((1,2,0)))





#将条件逻辑表述为数组运算
arrx=np.array([1.1,1.2,1.3,1.4])
arry=np.array([2.1,2.2,2.3,2.4])
cond=np.array([True,False,True,False])
t=np.where(cond,arrx,arry)
print(t)



arr=np.random.randn(5,4)#正太分布的数据
print(arr.mean())
print(np.mean(arr))
print(arr.mean(axis=1))
#基本数组统计方法函数既可以当作数组的实例方法调用，也可以当作顶级Numpy函数使用
#mean和sum这类函数可以接受一个axis参数，用于统计该轴上的


#排序
#和python内置的列表类型一样，numpy数组也可以用sort就地排序





#数组的合并和拆分
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
a=np.concatenate([arr1,arr2],axis=0)
print(a)
b=np.concatenate([arr1,arr2],axis=1)
print(b)


#元素的重复操作
#repeat
arr=np.arange(3)
print(arr.repeat(3))
print(arr.repeat([2,3,4]))#将不同的元素重复不同的次数
from numpy.random import randn
arr4=randn(2,2)
print(arr4)
print(arr4.repeat(2,axis=1))
print(arr4.repeat([2,3],axis=0))#将不同元素按行重复不同次数
print(arr4.repeat([2,3],axis=1))#将不同元素按列重复不同次数

#tile：铺瓷砖，沿着指定轴向堆叠数组的副本
print('before tile',arr4)
print(np.tile(arr4,2))
print(np.tile(arr4,(3,2)))




#广播：不同形状的数组之间算术运算执行的方式
#广播的原则：如果两个数组的后缘维度的轴长度相符或者其中一方的长度为1，则认为他们是广播兼容的


#values[::-1]产生一个反序的列表

#不等分，切蛋糕
import numpy as np
a=np.arange(12).reshape(3,4)
#print(a)
print(np.split(a,[1,2],axis=1))
b=np.split(a,[1,2],axis=1)
print(b)