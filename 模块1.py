# 此文件主要展示numpy库的使用

import numpy as np
# numpy 属于科学运算模块
# numpy中进行运算需要将所有的数据转换成数组对象
a = np.zeros((3,2)) # 创建一个3行2列的全0数组
n1 = a.shape # 查看数组的形状
n2 = a.dtype # 查看数组的数据类型
n3 = a.itemsize # 查看数组中每个元素的字节数
np.arange(3,7) # 创建一个从3到6递增的数组
np.arange(9,1) # 创建一个从9到1递减的数组
np.linspace(0,1,5) # 创建一个从0到1均匀分成5份的数组
np.random.rand(3,2) # 创建一个3行2列的随机数组
a.astype(np.int32) # 转换数组中的数据类型

# 尺寸相同的数组可以直接进行加减运算
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
print(array_1 + array_2)
# 使用dot会将两个向量进行点乘运算
b = np.dot(array_2,array_1)
print(b) # 即对应位置相乘后相加
# 使用@可进行矩阵乘法
array_3 = np.array([[1,2],
                    [3,4]])
array_4 = np.array([[5,6],
                    [7,8]])
c = array_3 @ array_4
print(c) # 矩阵乘法

i = np.array([1,2,3])
p = np.sin(i)  # 分别求正弦
p1 = np.cos(i) # 分别求余弦
print(p,p1)
# 也可以使用numpy数组与数字进行相乘
i1 = i * 5 # 该操作称为广播
# 不同尺寸的数组也可以进行相加减
# 运算前numpy会将这两个数组扩展至相同的尺寸 再将相同位置的相加减
o = np.array([1,2,3])
l = np.array([[1,2,3],
             [4,5,6]])
wpp = o + l
print(wpp)

o.max() # 返回最大元素
o.min() # 返回最小元素
o.argmax() # 返回最大元素索引
o.argmin() # 返回最小元素索引
o.sum() # 返回数据总和
o.mean() # 返回数据平均值
o.var() # 方差
o.std() # 标准差
# 以上函数对于多维数组可以设置新的参数axis
# axis的作用为指定维度
# 0表示按列进行操作，1表示按行进行操作
# 例如：
a = np.array([[1,2,3],
              [4,5,6]])
b = np.sum(a,axis=0) # 按列求和
c = np.sum(a,axis=1) # 按行求和
print(b,c)
# 获取数组中的元素的语法与python中列表相同
# 如：我想获取a中第一行第二列的元素(2)
print(a[0][1])
# 也可以使用切片获取多行多列的元素
print(a[0:2,1:3])
# 也可以使用布尔数组进行索引
# 也可以使用条件语句进行筛选
# 例如：
a = np.array([1,2,3,4,5])
b = np.array([True,False,True,False,True])
c = a[b] # 筛选出b中为True的元素
print(c) # 输出[1 3 5]

# numpy也可以进行图片处理
# 需要搭配pillow库使用
from PIL import Image
# 读取图片
im = Image.open('test.jpg')
# 显示图片
im.show()
# 还有其他一些操作 这里不再做更多展示