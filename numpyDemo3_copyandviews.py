import numpy as np

###
#   Copies and Views
#       When operating and manipulating arrays, their data is sometimes
#   copied into a new array and sometimes not. There are three cases:
#       I. No Copy at All
#       II. View or Shallow Copy
#       III. Deep Copy
#       IV. functions and methods overview
#           refer to: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview
###

###
# I. No copy at all
#       assignment: eg a=b; b change a change.
#       function calls make no copy. python passes mutable objects as references.
###
m = np.arange(12)
n = m
print("n is m: ", end='')
print(n is m)
n.shape=3,4 # change the shape of n
print("m.shape: ", end='')
print(m.shape)
def f(x):
    print(id(x))
print("id(m): ", end='')
print(id(m)) # id is a unique identifier of an object
print("f(m): ", end='')
print(f(m))

###
# II. View or shallow copy
#       Different array objects can share the same data.
#       view(): The view method creates a new array object that looks at the same data.
#       slice: slicing an array returns a view of it
###
# view() function
o = m.view()
print("o is m: ", end='')
print(o is m)
print("o.base is m: ", end='')
print(o.base is m)
print("o.flags.owndata: ", end='')
print(o.flags.owndata)
o.shape = 2,6 # m's shape doesn't change
print("m.shape: ", end='')
print(m.shape)
o[0,4] = 1234   # m's data change
print("o: ")
print(o)
print("m: ")
print(m)

# slice returns view
p = m[:, 1:3] # spaces added for clarity; could also be writen"m[:,1:3]"
print("m: ")
print(m)
print("p: ")
print(p)
p[:]=10 # p[:] is a view of m. Note the difference between p=10 and p[:]=10
print("p: ")
print(p)
print("m: ")
print(m)

###
# III. Deep Copy
#       copy(): the copy method makes a complete copy of the array and its data.
###
q = m.copy() # a new array object with new data is created.
print("q is m: ", end='')
print(q is m)
print("q.base is m: ",end='')
print(q.base is m)
q[0,0] = 9999
print("q: ")
print(q)
print("m: ")
print(m)

###
# IV. Functions and methods overview
# refer to :
#   https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#functions-and-methods-overview
###