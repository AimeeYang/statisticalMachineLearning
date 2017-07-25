import numpy as np
from numpy import newaxis

###
# learning record while learning
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
###

# ###
# # Shape Manipulation
# # I changing the shape of an array
# # II stacking together different array
# # III splitting one array into several smaller ones
# ###
#
# ###
# # I changing the shape of an array
# ###
#
# # The shape of an array can be changed with various commands.
# #    Note that the following three commands all return a modified array,
# # but do not change the original array.
# #   reshape vs resize: resize modify array itself, reshape not, namely
# # reshape return a new array.
#
# f = np.floor(10*np.random.random((3,4)))
# print("f: ")
# print(f)
# print("f.ravel(): ")
# print(f.ravel())
# print("f.reshape(6,2): ")
# print(f.reshape(6,2))
# print("f.T: ")
# print(f.T)
# print("f.T.shape: ",end='')
# print(f.T.shape)
# print("f.shape: ", end='')
# print(f.shape)
# # reshape vs resize
# #    If a dimension is given as -1 in a reshaping operation,
# # the other dimensions are automatically calculated, namely
# # the remain dimension's value is auto calculated.
# print("f.reshape(2,-1): ") # equal to f.reshape(2,6)
# print(f.reshape(2,-1))
# print("f: ")
# print(f)
# print("f.resize((2,6)): ")
# print(f.resize((2,6)))
# print("f after f.resize((2,6)): ")
# print(f) # after resize function the array itself changed


# ###
# # II stacking(堆放) together different arrays
# # 1. np.hstack, np.vstack
# # 2. np.column_stack
# # 3. For arrays of with more than two dimensions,
# #       hstack stacks along their second axes,
# #       vstack stacks along their first axes,
# #       concatenate allows for an optional arguments giving the number of the axis
# #           along which the concatenation should happen
# # NOTE:
# #   In complex cases, r_ and c_ are useful for creating arrays
# # by stacking numbers along ONE axis. They allow the use of range
# # literals (" :").
# #   When used with arrays as arguments, r_ and c_ are similar to vstack
# # and hstack in their default behavior, but allow for an optional
# # argument giving the number of the axis along with to concatenate.
# ###
#
# # Several arrays can be stacked together along different axes
# g = np.floor(10*np.random.random((2,2)))
# print("g: ")
# print(g)
# h = np.floor(10*np.random.random((2,2)))
# print("h: ")
# print(h)
# print("np.vstack((g,h)): ")
# print(np.vstack((g,h)))
# print("np.hstack((g,h)): ")
# print(np.hstack((g,h)))
#
# #    The function column_stack stacks 1D array as columns into a 2D array.
# # only for 1D arrays <=> vstack.\
# #    column_stack 维数与参数无关，只返回2维 only return 2D array, no matter how many parameters / axes.
# #       print("np.column_stack((i[:,newaxis], j[:,newaxis], k[:, newaxis])): ")
# #    vstack/hstack 维数和传入的参数有关，随参数的维度计算而得
# print("np.column_stack((g,h)): ") # with 2D array
# print(np.column_stack((g,h)))
#
# i = np.array([4,2])
# j = np.array([2,8])
# k = np.array([5,6])
# print("i[:,newaxis]: ")
# print(i[:,newaxis]) # This allows to have a 2D colunms vector
# print("conlumn_stack VS vstack: ")
# print("np.column_stack((i[:,newaxis],j[:,newaxis])): ")
# print(np.column_stack((i[:,newaxis],j[:,newaxis])))
# print("np.column_stack((i[:,newaxis], j[:,newaxis], k[:, newaxis])): ")
# print(np.column_stack((i[:,newaxis], j[:,newaxis], k[:, newaxis])))
# print("np.vstack((i[:,newaxis], j[:,newaxis])): ")
# print(np.vstack((i[:,newaxis], j[:,newaxis])))
# print("np.vstack((i[:,newaxis], j[:, newaxis], k[:, newaxis])): ")
# print(np.vstack((i[:,newaxis], j[:, newaxis], k[:, newaxis])))

###
# III. splitting one array into several smaller ones
#   分区方法：以或者均分或者指定分区区/‘点’ 的分配方式分割， ‘点’特殊，不过中间段为[]
#   np.hsplit: split an array along its horizontal axis, 以或者均分或者指定分区区/‘点’ 的分配方式分割
#           either by specifying the number of equally shaped arrays return,
#           or by specifying the colunms after which the division should occur
#   np.vsplit: 分区方法同hsplit，只是方向不同于hsplit, 为vertical axis.
#   np.array_split: 分区方法同hsplit, 不同在于可以指定along which axis to split.
###
l = np.floor(10*np.random.random((2,12)))
print("l: ")
print(l)
print("np.hsplit(l, 3): ")
print(np.hsplit(l, 3)) # split l into 3 # 均分
print("np.hsplit(l, (3,4)): ")
print(np.hsplit(l, (3,4))) # split l after the third and the forth column 分区区 [0,2] [3] [4,12]
print("np.hsplit(l, (3,3)): ")
# split l after the third column 分区点 但仍然返回3段，不过中间为array([],shape(2,0), dtype=float64)
print(np.hsplit(l, (3,3)))
print("np.hsplit(l, (3)): ")
print(np.hsplit(l, (3))) # 同均分 the same with print(np.hsplit(l, 3))
print("np.hsplit(l, (3, 5)): ")
print(np.hsplit(l, (3, 5))) # 分区区 [0,2] [3,4] [5,12]




