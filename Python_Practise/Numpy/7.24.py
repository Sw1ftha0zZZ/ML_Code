#19.7.24
#ndarray：一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组
#用于对整组数据进行快速运算的标准数学函数（无需编写循环）

#ndarray是一个通用的同构数据多维容器，所有元素必须是相同类型的
#每个数组都有一个shape和一个dtype

#创建ndarray
#将列表转换为数组
import numpy as np
data1=[6,7.5,8,12,3]
arr1=np.array(data1)
print(arr1,arr1.dtype)
print (np.zeros((3,6)))

data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
print(arr2,arr2.ndim,arr2.shape,arr2.dtype)
#除非显式说明，np.array会尝试为新创建的这个数组推断出一个
#较为合适的数据类型，数据类型保存在dtype对象中


#empty返回的是一些未初始化的垃圾值
print(np.empty((2,3,2)))


#arange是python内置函数range的数组版
print(np.arange(15))
a=np.arange(15)
b=a.reshape((3,5))
print(b)

arr=np.array([2.1,3.2,4.3])
arr.astype(np.int32)
print(arr.astype(np.int32))
#通过ndarray的astype方法可以显式地转换dtype



#不同大小的数组之间的运算叫做广播

