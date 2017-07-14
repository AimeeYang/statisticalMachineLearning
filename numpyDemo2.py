import numpy as np

###
# learning record while learning
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#splitting-one-array-into-several-smaller-ones
###

###
# Shape Manipulation
# I changing the shape of an array
# II stacking together different array
###

###
# I changing the shape of an array
###

# The shape of an array can be changed with various commands.
#    Note that the following three commands all return a modified array,
# but do not change the original array.
#   reshape vs resize: resize modify array itself, reshape not, namely
# reshape return a new array.

f = np.floor(10*np.random.random((3,4)))
print("f: ")
print(f)
print("f.ravel(): ")
print(f.ravel())
print("f.reshape(6,2): ")
print(f.reshape(6,2))
print("f.T: ")
print(f.T)
print("f.T.shape: ",end='')
print(f.T.shape)
print("f.shape: ", end='')
print(f.shape)
# reshape vs resize
#    If a dimension is given as -1 in a reshaping operation,
# the other dimensions are automatically calculated, namely
# the remain dimension's value is auto calculated.
print("f.reshape(2,-1): ") # equal to f.reshape(2,6)
print(f.reshape(2,-1))
print("f: ")
print(f)
print("f.resize((2,6)): ")
print(f.resize((2,6)))
print("f after f.resize((2,6)): ")
print(f) # after resize function the array itself changed


###
# stacking together different arrays
###




