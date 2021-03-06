import numpy as np

###
# learning record while learning
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
###

###
#   Python list vs numpy array
# 标准Python的列表(list)中，元素本质是对象。
# Python list不关心数据项类型，即任一数据项可以是任意类型 => 运算性能低于numpy的ndarray
# 如：L = [1, 2, 3]，需要3个指针和三个整数对象，对于数值运算比较浪费内存和CPU。
# 因此，Numpy提供了ndarray(N-dimensional array object)对象：存储单一数据类型的多维数组。
# refer from teacher zoubo
###


###
# I. basic concept:
# numpy ndarray
# basic property
# TODO 整理笔记;
# reshape vs shape：
#       reshape 原array shape不变
#       shape   原array shape变；
# shape 的类型是tuple
# shape: (,,) : 从左至右对应 array “由外到内”
#             : 其他理解方法： 对应坐标轴 shape=(z,y,x) ndarray= [[[x个] y个] z个]
# axis 计数从0开始，从array “由内到外” 开始。
#       与shape(z,y,x)对应：x 的axis=0
#                           y 的axis=1
#                           z 的axis=2
# 索引的时候[:,:,:] ','前后对应到array是由“由外到内”的，
#       即第一个‘：’对应shape的z, 对应axis=2
#           二                   y,     axis=1
#           三                   x,     axis=0
#
# 综上：shape & indexing: -> （在array上的方向） **！！！
#       axis:             ->
#
# 更改元素类型：
#       如果更改元素类型，可以使用astype安全的转换；但不要强制仅修改元素类型，
#   如下面这句，将会以int来解释单精度float类型
#       d.dtype = np.int
#       f = d.astype(np.int) # Better
###

# a = np.arange(24).reshape(2,3,4)
# a1 = np.array([[1],[2]])
# b = np.arange(8).reshape(2,4)
# print("a: ")
# print(a)
# print("a.shape: ",end='') # print without newline in python 3
# print(a.shape)
# print(type(a.shape))
# print(type(a1.shape))
###
# AXIS dimension rank:
#       In numpy, dimensions are called axes.
#               the number of axes is rank.
#   BY sort():
#       axis: 计数方向 ->
#       在sort中， 意为沿着指定axis 排序 (asc)
###
a2 = np.random.random((2,2))
print("a2: ")
print(a2)
print("a2.ndim: ", end='')
print(a2.ndim)
print("np.sort(a2,axis=0): ")
print(np.sort(a2,axis=0))
print("np.sort(a2, axis=1): ")
print(np.sort(a2, axis=1))
# print("np.sort(a2, axis=2): ") # ValueError: axis(=2) out of bounds
# print(np.sort(a2, axis=2))

a3 = np.random.random((3,4))
print("a3: ")
print(a3)
print("a3.ndim: ",end='')
print(a3.ndim)
print("np.sort(a3, axis=0):")
print(np.sort(a3, axis=0))
print("np.sort(a3, axis=1):")
print(np.sort(a3, axis=1))
# print("np.sort(a3, axis=0):")
# print(np.sort(a3, axis=2))

###
# reshape use of -1 : 只是为了方便，减少运算(因为自动算出其余维度)
#       eg. np.arange(0, 60, 10).reshape((-1, 1))
#         <=> np.arange(0, 60, 10).reshape((6, 1)) # 此处自动算出行的个数
# 综上： 当某个轴为-1时，将根据数组元素的个数自动计算此轴的长度
print(np.arange(0, 60, 10).shape)
print(np.arange(0, 60, 10).reshape(-1))
print(np.arange(0, 60, 10).reshape(-1).shape)
print(np.arange(0, 60, 10).reshape((-1, 1)))
print(np.arange(0, 60, 10).reshape((-1, 1)).shape)
print(np.arange(0, 60, 10).reshape((6, 1)))
print(np.arange(0, 60, 10).reshape((-1, 3)))
print(np.arange(0, 60, 10).reshape((-1, 3)).shape)
print(np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6))
# [[ 0  1  2  3  4  5]
#  [10 11 12 13 14 15]
#  [20 21 22 23 24 25]
#  [30 31 32 33 34 35]
#  [40 41 42 43 44 45]
#  [50 51 52 53 54 55]]


# print("a.ndim: ", end='')
# print(a.ndim)
# print("a.itemsize: ", end='')
# print(a.itemsize)
# print("a.size: ", end='')
# print(a.size)
# print("a.dtype: ", end='')
# print(a.dtype, end='')
# print(", a.dtype.name: ", end='')
# print(a.dtype.name)
# print("type(a): ", end='')
# print(type(a))
#
# print('')
# print("b: ")
# print(b)
# print("b.shape: ", end='')
# print(b.shape)
# print("b.ndim: ", end='')
# print(b.ndim)
# print("b.itemsize: ", end='')
# print(b.itemsize)
# print("b.size: ", end='')
# print(b.size)
# print("b.dtype: ", end='')
# print(b.dtype, end='')
# print(", b.dtype.name: ", end='')
# print(b.dtype.name)
# print("type(b): ", end='')
# print(type(b))

###
# II. operation
#   create
#   print
#   basic operation
#   indexing, slicing and iterating
###

# # create by array/ndarray
# c1 = np.array([2,3,4])
# c2 = np.array([(1,2),(3,4)],dtype=complex)
#
# # create with size and placeholder, namely shape
# c3 = np.zeros((3,4)) # shape
# c4 = np.ones((2,3,4))
# c5 = np.empty((2,3))
#
# # create with range,step => a,b
# # create with linspace, fixed num
# c6 = np.linspace(0, 2, 9) # size = 9

# # other:
# # array, zeros, zeros_like, ones, ones_like, empty, empty_like,
# # arange, linspace,
# # numpy.random.rand, numpy.random.randn,
# # fromfunction, fromfile
#
# # print
# # default: print ..., when itemsize is big
# # deactive default: np.set_printoptions(threshold='nan')
# np.set_printoptions(threshold='nan')

# basic operation
# 总： 支持一般的矩阵操作，其他运算操作(+，*)相当于map，并map到每个元素
#      一些操作也支持指定轴
#      注意操作是否产生新array
# TODO 整理操作example based on the tutorial，并注意整理操作是否产生新array, 可参考 numpyDemo3_copyandviews.py
#


# indexing, slicing and iterating
# I one-dimensional arrays can be indexed, sliced and iterated most like
#   list and other Python sequence
# II multidimensional
#   1. 单值
#       和坐标类似，如二维[rowindex,colindex]
#   2. 某块
#       各个维度上slice组合


# # one-dimensional
# d = np.arange(10)**3
# print("d: ")
# print(d)
# # indexing
# print("d[2]: ", end='')
# print(d[2])
#
# # slicing
# print("d[2:5]: ",end='') # 前包后不包
# print(d[2:5])
# print("after d[:6:2] = -1000, d: ") # [:6:2] <=> [0:6:2], step=2
# d[:6:2] = -1000
# print(d)
# print("d[ : :-1]: ") # <=> reversed
# print(d[ : :-1])
#
# # iterating
# for i in d:
#     print(i**(1/3))

# # II multidimensional array indexing, slicing & iterating
# def f(x, y):
#     return 10*x + y
#
# ###
# # """
# #     Construct an array by executing a function over each coordinate.
# #
# #     The resulting array therefore has a value ``fn(x, y, z)`` at
# #     coordinate ``(x, y, z)``.
# #
# #     Parameters
# #     ----------
# #     function : callable
# #         The function is called with N parameters, where N is the rank of
# #         `shape`.  Each parameter represents the coordinates of the array
# #         varying along a specific axis.  For example, if `shape`
# #         were ``(2, 2)``, then the parameters in turn be (0, 0), (0, 1),
# #         (1, 0), (1, 1).
# #     shape : (N,) tuple of ints
# #         Shape of the output array, which also determines the shape of
# #         the coordinate arrays passed to `function`.
# #     dtype : data-type, optional
# #         Data-type of the coordinate arrays passed to `function`.
# #         By default, `dtype` is float.
# #
# #     Returns
# #     -------
# #     fromfunction : any
# #         The result of the call to `function` is passed back directly.
# #         Therefore the shape of `fromfunction` is completely determined by
# #         `function`.  If `function` returns a scalar value, the shape of
# #         `fromfunction` would match the `shape` parameter.
# e = np.fromfunction(f, (5,4), dtype=int)
# # 上面相当于 传入f 如下 5*4个 (x,y)对  0 <= x <= 4; 0 <= y <= 3
# # ( (0,0) (0,1) (0,2),(0,3)
# #   (1,0) (1,1) (1,2),(1,3)
# #   (2,0) (2,1) (2,2),(2,3)
# #   (3,0) (3,1) (3,2),(3,3)
# #   (4,0) (4,1) (4,2),(4,3))
# #
# print("e: ")
# print(e)
#
# # indexing
# print("e[2,3]: ",end='')
# print(e[2,3]) # 此时相当于坐标（row, column)
# # 多维slice, [,] ',' 分隔各轴slice信息；如下
# print("e[0:5, 1]: ",end='') # 相当于row轴slice[0:5], column轴第1列; 有点类似矩阵切块
# print(e[0:5, 1])
# print("e[0:5, 1]: ", end='')
# print(e[0:5, 1])
# print("e[1:3, : ]: ")
# print(e[1:3, : ])
#
# # TRY SLICE WITH STEP IN EACH DIM => 多维slice在每个维度上的操作和一维的相同
# print("e[::2,::2]: ")
# print(e[::2,::2])
#
# #   when fewer indices are provided than the number of axes, the missing indices
# # are considered complete slices:
# #   dots(...) represent as many colons as needed to produce a complete indexing
# # tuple.
# # eg. x is a rank 5 array,
# # x[1,2,...] = x[1,2,:,:,:];
# # x[...,3] = x[:,:,:,:,3]
# # x[4,...,5,:] = x[4,:,:,5,:]
# print("e[-1]: ") # the same as e[-1,:]
# print(e[-1])
#
# ### iterating multidimensional arrays
# # 维度顺序按从左至右
# print("iterating multidimensional")
# for row in e:
#     print(row)
#
# #    if wants to perform an operation on each element in the array,
# # can use the flat attribute which is an iterator over all the
# # elements of the array
# for element in e.flat:
#     print(element)













