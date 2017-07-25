#!/usr/bin/python
# -*- coding:utf-8 -*-

###
# code refer chinahadoop course machine learning
#
###

import csv
import numpy as np
import pandas as pd

#手写读取数据
def nolibLoad(path):
    f = open(path) # in python3 no file function file(path)
    x = []
    y = []
    for linenum, data in enumerate(f):
        if linenum == 0: #ignore header
            continue
        data = data.strip()
        if not data:
            continue
        # d = map(float, d.split(',')) in python 2.7
        dataX = list(map(float, data.split(',')[0:-1]))
        dataY = strLabelCovertToIntLabel(data.split(',')[-1])
        # x.append(data[1:-1])
        # y.append(data[-1])
        x.append(dataX)
        y.append(dataY)
    f.close()
    print(x)
    print(y)
    x = np.array(x)
    y = np.array(y)
    return x,y

# Python自带库
def pythonlibLoad(path):
    #f = open(path, 'rb') # read as binary
    x = []
    y = []
    f = open(path)
    print(f)
    d = csv.reader(f) # header as a line
    d2 = csv.DictReader(f) # read with the first line as header
    # for line in d:
    #     print(line)
    #     break
    for line2 in d2: # start from the second line; the first line used as header
        if not line2:
            continue
        x.append([line2['sepal_length'],line2['sepal_width'],line2['petal_length'],line2['petal_width']])
        y.append(strLabelCovertToIntLabel(line2['class']))

    f.close()
    x=np.array(x)
    y=np.array(y)
    return x,y

# numpy读入
def numpyLoad(path):
    # d = np.load()
    # numpy loadtxt with converters
    d = np.loadtxt(path,dtype=float, delimiter=',', converters={4: strLabelCovertToIntLabel},skiprows=1)
    #d = np.loadtxt(path,delimiter=',',skiprows=1,dtype='object')

    #print(d)
    x, y = np.split(d,(4,),axis=1)
    print("x: ")
    print(x)
    print("y: ")
    print(y)
    return x, y
    ###
    # numpy array split (numpy ndarray 切片方法)
    # refer: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html#indexing-with-arrays-of-indices
    #
    # 1. 通过numpy 自带库 hsplit, vsplit, array_split (水平，竖直，任意轴)
    # 2. 通过fancy indexing and index tricks
    #       2.1 indexing with Arrays of Indices
    #       2.2 indexing with Boolean Arrays
    #       2.3 the ix_() function
    #       2.4 Indexing with strings
    ###

    # 1. 通过numpy自带split方法，此处根据x,y切分需要，利用hspit方法




    # # [0,2,4] part is the index part; index of colunm, start from 0
    # # 3: is the start row of d, row start from 0
    # print(d[3:,[0,2,4]])
    # i = np.array([True,True,True,True,False])
    # #  d[i,3] 3 colunm index, start from 0
    # print(d[i,3])
    # print(d[i])
    # # TODO 补全x,y with numpy array split


# pandas读入
def pandaLoad(path):
    # pandas 提供若干 file type 的 read
    d = pd.read_csv(path)
    print(d)
    #TODO 补全x,y


### for iris data
def strLabelCovertToIntLabel(labelstr):
    ### in python3 use dictionary instead of switch,
    ### below with default value -1 when labelstr is not found
    return{
        b'Iris-setosa': 1,
        b'Iris-versicolor': 2,
        b'Iris-virginica': 3
    }.get(labelstr,-1) # -1 is the default value when labelstr is not found

    # return {
    #     'Iris-setosa': 1,
    #     'Iris-versicolor': 2,
    #     'Iris-virginica': 3
    # }[labelstr] # without default value

### for test
if __name__ == "__main__":
    path = "./data/iris.data.txt"
    # x, y = nolibLoad(path)
    x,y = numpyLoad(path)

    # path = "./data/iris.data.csv"
    # x, y = pythonlibLoad(path)
    print(x)
    print(y)