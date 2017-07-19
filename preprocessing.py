#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np


###
#   For Iris data set, change string labels to integer labels.
# So that load data with numpy or pandas will be convenient.
###

def preprocess_changeLabelType(orifile, newfile, convertfunc):
    data = np.loadtxt(orifile,delimiter=',',skiprows=0)
    print(data.shape)
    print(data.dtype)
    print(data.size)
    x=[]
    y=[]
    for i in range(data.shape[0]):
        print(i)
        print(data[i])
        break;


### for iris data
def strLabelCovertToIntLabel(labelstr):
    ### in python3 use dictionary instead of switch,
    ### below with default value -1 when labelstr is not found
    return{
        'Iris-setosa': 1,
        'Iris-versicolor': 2,
        'Iris-virginica': 3bv
    }.get(labelstr,-1) # -1 is the default value when labelstr is not found

    # return {
    #     'Iris-setosa': 1,
    #     'Iris-versicolor': 2,
    #     'Iris-virginica': 3
    # }[labelstr] # without default value

# below for test.
if __name__ == "__main__":
    orifile = "./data/iris.data.txt"
    newfile = "./data/iris.cov.txt"
    preprocess_changeLabelType(orifile,newfile, strLabelCovertToIntLabel)