import numpy as np

###
# learning record while learning
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
###

###
# I. basic concept:
# numpy ndarray
# basic property
# TODO 整理笔记
###

a = np.arange(24).reshape(2,3,4)
b = np.arange(8).reshape(2,4)
print("a: ")
print(a)
print("a.shape: ",end='') # print without newline in python 3
print(a.shape)
print("a.ndim: ", end='')
print(a.ndim)
print("a.itemsize: ", end='')
print(a.itemsize)
print("a.size: ", end='')
print(a.size)
print("a.dtype: ", end='')
print(a.dtype, end='')
print(", a.dtype.name: ", end='')
print(a.dtype.name)
print("type(a): ", end='')
print(type(a))

print('')
print("b: ")
print(b)
print("b.shape: ", end='')
print(b.shape)
print("b.ndim: ", end='')
print(b.ndim)
print("b.itemsize: ", end='')
print(b.itemsize)
print("b.size: ", end='')
print(b.size)
print("b.dtype: ", end='')
print(b.dtype, end='')
print(", b.dtype.name: ", end='')
print(b.dtype.name)
print("type(b): ", end='')
print(type(b))

###
#