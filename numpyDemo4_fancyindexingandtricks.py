import numpy as np

###
# learning record while learning
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
###

###
# Fancy indexing and index tricks
#       In addition to indexing by integers and slices,
#   arrays can be indexed by arrays of intergers and arrays of booleans.
#   I. indexing with arrays of indices
#   II. indexing with boolean arrays
#   III. the ix_() function
###

# ###
# #   I. indexing with arrays of indices
# #       indices一维
# #           indexed array一维：用indexed array做数据源，用indice做新array的shape并提供所需数据在数据源上的索引
# #               如: r[s] r是数据源，提供数据；s提供新array的shape 以及所需数据在源数据的位置
# #           当indexed array是多维：indice 索引指indexed array的第一维；值为第一维上指定位置的值
# #       indices多维：区分由indices决定的shape和索引值
# #
# # ###
# r=np.arange(12)**2
# print("r: ")
# print(r)
# s=np.array([1,1,3,8,5]) # an array of indices
# r[s] # the emlements of r at the positions i
# print("r[s]: ")
# print(r[s])
# t=np.array([[3,4],[9,7]])
# print("r[t]: ")
# print(r[t])
#
# #   When the indexed array a is multidimensional, a single array of indices
# # refers to the first dimension of a.
# palette=np.array([[0, 0, 0],       # black
#                    [255,0,0],       # red
#                    [0,255,0],       # green
#                    [0,0,255],       # blue
#                    [255,255,255]    #white
#                    ])
# image=np.array([[0,1,2,0],
#                 [0,3,4,0]])     # each value corresponds to a color in the palette；每个值对应行标
# print("palette[image]")
# print(palette[image])           # the (2,4,3) color image
#
# # We can also give indexes for more than one dimension.
# # The arrays of indices for each dimension must have the same shape.
# u=np.arange(12).reshape(3,4)
# print("u: ")
# print(u)
# indices_i=np.array([[0,1],
#                   [1,2]])   # indices for the first dim of u
# indices_j=np.array([[2,1],
#                     [3,3]])  # indices for the second dim
#
# # 0. indices_i, indices_j equal shape原则
# # 1. indices_i & indices_j 共同决定了新array的shape => 2 * 2, 2*2 => 新array's shape is: 2*2
# # 2. 新array's element 对应到源data的位置:
# #    2.1 indices_i: 第一维坐标
# #    2.2 indices_j: 第二维坐标
# #    2.3 拼接成的坐标对如下:
# #       (0, ), (1, )    (, 2), (, 1)    (0, 2), (1, 1)
# #                    +               =
# #       (1, ), (2, )    (, 3), (, 3)    (1, 3), (2, 3)
# #    2.4 由坐标对在源数据上定位具体数据，以及新array的shape => 得到新array 为:
# #       [[2, 5],
# #        [7, 11]]
# print("u[indices_i,indices_j]: ")
# print(u[indices_i,indices_j])  # indices_i and indices_j must have equal shape
#
# # 0. equal shape 原则 => 2*2, 2*2 => 2*2
# # 1. indices_i, & 常数 2 共同决定新array的shape：此处有indices_i 决定，即为 2*2
# # 2. 新array's element 对应到源data的位置:
# #    2.1 indices_i: 第一维坐标
# #    2.2 2: 第二维坐标，此处常数2，相当于indices值为: [[2, 2], [2, 2]]
# #    2.3 拼接成的坐标对如下:
# #       (0, ), (1, )    (, 2), (, 2)    (0, 2), (1, 2)
# #                    +               =
# #       (1, ), (2, )    (, 2), (, 2)    (1, 2), (2, 2)
# #    2.4 由坐标对在源数据上定位具体数据，以及新array的shape => 得到新array 为:
# #       [[2, 6],
# #        [6, 10]]
# print("u[indices_i, 2]: ")
# print(u[indices_i, 2])
# # 同上，第二维坐标为[[3,3],[3,3]]
# print("u[indices_i, 3]: ")
# print(u[indices_i, 3])
# # print("u[indices_i, 4]: ")
# # print(u[indices_i, 4]) # IndexError: index 4 is out of bounds for axis 1 with size 4
#
# # 0. equal shape 原则 => 由交叠部分满足 3*2*2, 2*2 => 3*2*2
# # 1. 新array's shape:
# #    1.1 : 决定新array外层维度(或由左至右看左边维度)=> 源数据的第一维的个数上(3行)/源数据第一维索引上,:<=> 0:2； 即从索引0到索引2
# #    1.2 indices_j 决定新array shape的里层维度(或由左至右看右边维度)，即2*2
# #    1.3 由1.1和1.2得新array的shape为 3*2*2
# # 2. 新array's element 对应到源data的位置:
# #    2.1 : <=> 0,1,2; 且是第一维的坐标,相当于
# #       [[[0,0],[0,0]],
# #        [[1,1],[1,1]],
# #        [[2,2],[2,2]]]
# #    2.2 indices_j: 第二维坐标
# #    2.3 拼接成的坐标如下:
# #       (0, 2),(0, 1)
# #       (0, 3),(0, 3)
# #
# #       (1, 2),(1, 1)
# #       (1, 3),(1, 3)
# #
# #       (2, 2),(2, 1)
# #       (2, 3),(2, 3)
# #    2.4 由坐标对在源数据上定位具体数据，以及新array的shape => 得到新array 为:
# #       [[[2, 1],
# #         [3, 3]],
# #        [[6, 5],
# #         [7, 7]],
# #        [[10, 9],
# #         [11, 11]]
# print("u[:,indices_j]: ")
# print(u[:,indices_j]) # res's shape: 3*2*2
#
# # 0. equal shape 原则 => 由交叠部分满足 2*2,2*2*4 => 2*2*4
# # 1. 新array's shape:
# #    1.1 indices_i 决定新array外层维度(或由左至右看左边维度),即2*2
# #    1.2 : 决定新array shape的内层维度(或由左至右看右边维度)=> 源数据的第二维的个数上(4列)/源数据第二维索引上,:<=> 0:3； 即从索引0到索引3
# #    1.3 由1.1和1.2得新array的shape为 2*2*4
# # 2. 新array's element 对应到源data的位置:
# #    2.1 indices_i: 第一维坐标
# #    2.2 : <=> 0,1,2,3; 且是第二维的坐标,相当于
# #       [[[0,1,2,3],
# #         [0,1,2,3]],
# #        [[0,1,2,3],
# #         [0,1,2,3]]]
# #    2.3 拼接成的坐标如下:
# #       (0, 0),(0, 1),(0, 2),(0, 3)
# #       (1, 0),(1, 1),(1, 2),(1, 3)
# #
# #       (1, 0),(1, 1),(1, 2),(1, 3)
# #       (2, 0),(2, 1),(2, 2),(2, 3)
# #    2.4 由坐标对在源数据上定位具体数据，以及新array的shape => 得到新array 为:
# #       [[[0, 1, 2, 3],
# #         [4, 5, 6, 7]],
# #        [[4, 5, 6, 7],
# #         [8, 9, 10, 11]]]
# print("u[indices_i,:]: ")
# print(u[indices_i,:]) # res's shape: 2*2*4
# # try indices_i & indices_j 为3*3的情况；1*1的情况 => 原理与2*2相同
# print("============================")
# indices_i_3 = np.array([[0,1,2],
#                         [2,1,0],
#                         [0,1,1]])# 3*3,值为第一维上索引
# indices_j_3 = np.array([[0,1,2],
#                         [3,2,1],
#                         [0,3,1]])# 3*3,值为第二维上索引
#
# print("u[indices_i_3,indices_j_3]: ")
# print(u[indices_i_3,indices_j_3])  # indices_i and indices_j must have equal shape
#
# print("u[indices_i_3, 2]: ")
# print(u[indices_i_3, 2])
# print("u[2, indices_j_3]: ")
# print(u[2, indices_j_3])
#
# print("u[:,indices_j_3]: ")
# print(u[:,indices_j_3]) # res's shape: 3*3*3
# # 新array[0]处的坐标对为
# # (0, 0),(0, 1),(0, 2),(0, 3)
# # (1, 0),(1, 1),(1, 2),(1, 3)
# # (2, 0),(2, 1),(2, 2),(2, 3)
# print("u[indices_i_3,:]: ")
# print(u[indices_i_3,:]) # res's shape: 3*3*4
# print("u[indices_i_3,:][0,0,0]: ")
# print(u[indices_i_3,:][0,0,0]) #0
# print("u[indices_i_3,:][0]: ")
# print(u[indices_i_3,:][0])
# #[[ 0  1  2  3]
# # [ 4  5  6  7]
# # [ 8  9 10 11]]
#
# #    Naturally, we can put indices_i and indices_j in a sequence (say a list) and
# #  then do the indexing with the list.
# #    However, we can not do this by putting indices_i and indices_j into array,
# #  because this array will be interpreted as indexing the first dimension of a.
# indices=[indices_i, indices_j] # MUST BE LIST FORMART
# print("u[indices]: ")
# print(u[indices])
# wrong_indices=np.array([indices_i, indices_j])
# # u[wrong_indices]  # IndexError: index 3 is out of bounds for axis 0 with size 3
# u[tuple(wrong_indices)]  # the same as u[indices]
#
# # search of the maximum value of time-dependent series
# # linspace: 等差数列
# time=np.linspace(20, 145, 5)    # time scale, start,end, num
# data=np.sin(np.arange(20)).reshape(5,4) # 4 time-dependent series
# print("time: ")
# print(time)
# print("data: ")
# print(data)
# # 理解argmax(axis = 0)中参数axis的用法
# #   可以看做控制变量法中，其他axis值不变，只有指定的轴上数值变；
# #   如：data.argmax(axis=0),
# #   axis=1轴上值不变；比较max((0,0),(1,0),(2,0),(3,0),(4,0)),返回最大值所在的轴axis=0的index值
# # data.max(axis=0)中参数axis的理解同上
# ind=data.argmax(axis=0) #index of the maxima for each series
# print("ind: ")
# print(ind)
# tmp=data.argmax(axis=1)
# print("tmp: ")
# print(tmp)
# time_max=time[ind]  # times corresponding to the maxima
# print("time_max: ")
# print(time_max)
# data_max=data[ind, range(data.shape[1])]   # => data[ind[0],0],data[ind[1],1]
# print("data_max: ")
# print(data_max)
# # data[data.argmax(axis=0),range(data.shape[1])] = data.max(axis=0)
# print(np.all(data_max == data.max(axis=0)))
#
# # you can also use indexing with arrays as a target to assign to
# # however, when the list of indices contains repetitions, the assignment
# #   is done several times, leaving behind the last value.
# #   Be careful about the 同一索引出现多次的情况，在+= 的情况下，无论出现多少次，都只加一次
# #       v[[0,0,2]]+=1 => 在索引0处的值只增加1； this is because python requires "a+=1" to be
# #                       equivalent to "a=a+1"
# v=np.arange(5)
# print("v: ")
# print(v)
# v[[1,3,4]] = 99
# print("v after v[[1,3,4]] = 99: ")
# print(v)
# v[[0,0,2]] = [77, 88, 66]
# print("v after v[[0,0,2]] = [77, 88, 66]: ")
# print(v)
# v[[0,0,2]]+=1
# print("v after v[[0,0,2]]+=1: ")
# print(v)

# ###
# # II. indexing with boolean arrays
# #       When index arrays with arrays of (integer) indices we providing the
# #   list of indices to pick.
# #       With boolean indices the approach is different; we explicitly choose
# #   which items in the array we want and which ones we don't.
# #       1. indexing using boolean arrays, that have the same shape as the original array.
# #       2. indexing with boolean that is similar to integer indexing:
# #           for each dimension of the array we give a 1D boolean array selecting the slices we want.
# ###
#
# # 1. indexing using boolean arrays, that have the same shape as the original array.
# w = np.arange(12).reshape(3,4)
# x = w > 4   # x is a boolean with w's shape
# print("w:")
# print(w)
# print("x=w>4")
# print(x)
# print("w[x]")
# # 注意此处w[x]是一维的！！！
# print(w[x]) # w[x] 1d array with the selected elements
# # can be useful in assignments:
# w[x]=99     # all elements of 'w' greater than 4 becames 99
# print("after w[x]=99, w:")
# print(w)
#
# # example: mandelbrot :
# #               use boolean indexing to generate an image of the Mandelbrot set.
#
# # 2. indexing with boolean that is similar to integer indexing
# #       for each dimension of the array we give a 1D boolean array selecting the slices we want.
# y = np.arange(12).reshape(3,4)
# print("y: ")
# print(y)
# boolean_index_1 = np.array([False, True, True])     # first dim selection
# boolean_index_2 = np.array([True, False, True, False])  # second dim selection
# print("y[boolean_index_1,:]: ")
# print(y[boolean_index_1,:])     # selecting rows
# print("y[boolean_index_1]: ")
# print(y[boolean_index_1])       # y[boolean_index_1,:] <=> y[boolean_index_1]
# print("y[:,boolean_index_2]: ")
# print(y[:,boolean_index_2])     # selecting colunms
#
# # 注：下面例子的结果很特殊 ！！！
# print("y[boolean_index_1,boolean_index_2]: ")
# print(y[boolean_index_1,boolean_index_2])       # a weird thing to do

# todo 补充ix_()
###
# III. the ix_() function
#       The ix_ function can be used to combine different vectors so as to obtain
#    the result for each n-uplet.
###