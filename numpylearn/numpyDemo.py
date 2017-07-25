import numpy as np

###
# learning record while learning
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
###

###
# I. basic concept:
# numpy ndarray
# basic property
# TODO 整理笔记; 补reshape vs shape?
# shape 的类型是tuple
# shape: (,,) : 从左至右对应 array 由内到外
#             : 其他理解方法： 对应坐标轴 shape=(z,y,x) ndarray= [[[x个] y个] z个]
###

a = np.arange(24).reshape(2,3,4)
a1 = np.array([[1],[2]])
# b = np.arange(8).reshape(2,4)
# print("a: ")
# print(a)
# print("a.shape: ",end='') # print without newline in python 3
# print(a.shape)
print(type(a.shape))
print(type(a1.shape))
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













