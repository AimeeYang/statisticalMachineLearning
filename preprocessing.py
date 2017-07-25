#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np


###
#   For Iris data set, change string labels to integer labels.
# So that load data with numpy or pandas will be convenient.
###

# TODO use sklearn的数据预处理

def preprocess_changeLabelType(orifile, newfile,convertLabelfunc):
    data = np.genfromtxt(orifile ,delimiter=',', dtype=None,
                         names=('sepal_length','sepal_width','petal_length','petal_width','class'),skip_header=1) # 注意skiprows start from 1
    print(data.shape)
    print(data.dtype)
    print(data.size)
    x=[]
    y=[]
    # x = data[:99,0:1]
    # y = map(convertLabelfunc,data[:99,4])
    for i in range(data.shape[0]):
        print(i)
        print(data[i])
        if(data[i][4] != "Iris-virginica"):
            x.append(list(data[i])[0:4])
            y.append(convertLabelfunc(data[i][4]))
    np.savetxt(newfile,np.column_stack((x,y)),delimiter=',')
    #TODO 如何使数据类型保持不变


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

# below for test.
if __name__ == "__main__":
    orifile = "./data/iris.data.txt"
    newfile = "./data/iris.cov.csv"
    preprocess_changeLabelType(orifile,newfile, strLabelCovertToIntLabel)