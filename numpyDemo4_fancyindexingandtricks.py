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
###

###
#   I. indexing with arrays of indices
#       indices一维
#           indexed array一维：用indexed array做数据源，用indice做新array的shape并提供所需数据在数据源上的索引
#               如: r[s] r是数据源，提供数据；s提供新array的shape 以及所需数据在源数据的位置
#           当indexed array是多维：indice 索引指indexed array的第一维；值为第一维上指定位置的值
#       indices多维
#
# ###
r=np.arange(12)**2
print("r: ")
print(r)
s=np.array([1,1,3,8,5]) # an array of indices
r[s] # the emlements of r at the positions i
print("r[s]: ")
print(r[s])
t=np.array([[3,4],[9,7]])
print("r[t]: ")
print(r[t])

#   When the indexed array a is multidimensional, a single array of indices
# refers to the first dimension of a.
palette=np.array([[0, 0, 0],       # black
                   [255,0,0],       # red
                   [0,255,0],       # green
                   [0,0,255],       # blue
                   [255,255,255]    #white
                   ])
image=np.array([[0,1,2,0],
                [0,3,4,0]])     # each value corresponds to a color in the palette；每个值对应行标
print("palette[image]")
print(palette[image])           # the (2,4,3) color image

# We can also give indexes for more than one dimension.
# The arrays of indices for each dimension must have the same shape.
u=np.arange(12).reshape(3,4)
print("u: ")
print(u)
indices_i=np.array([[0,1],
                  [1,2]])   # indices for the first dim of u
indices_j=np.array([[2,1],
                    [3,3]])  # indices for the second dim
print("u[indices_i,indices_j]: ")
# TODO indices with 2d or below example not understand
print(u[indices_i,indices_j])  # indices_i and indices_j must have equal shape
print("u[indices_i, 2]: ")
print(u[indices_i, 2])
print("u[:,indices_j]: ")
print(u[:,indices_j])

#    Naturally, we can put indices_i and indices_j in a sequence (say a list) and
#  then do the indexing with the list.
#    However, we can not do this by putting indices_i and indices_j into array,
#  because this array will be interpreted as indexing the first dimension of a.
indices=[indices_i, indices_j]
print("u[indices]: ")
print(u[indices])
wrong_indices=np.array([indices_i, indices_j])
u[wrong_indices]
u[tuple(wrong_indices)]  # the same as u[indices]

# TODO below don't understand
# search of the maximum value of time-dependent series
time=np.linspace(20, 145, 5)    # time scale
data=np.sin(np.arange(20)).reshape(5,4) # 4 time-dependent series
print("time: ")
print(time)
print("data: ")
print(data)
ind=data.argmax(axis=0) # index of the maxima for each series
print("ind: ")
print(ind)
time_max=time[ind]  # times corresponding to the maxima
print("time_max: ")
print(time_max)
data_max=data[ind, range(data.shape[1])]   # => data[ind[0],0],data[ind[1],1]
print("data_max: ")
print(data_max)
print(np.all(data_max == data.max(axis=0)))
