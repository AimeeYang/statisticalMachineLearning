#!/usr/bin/python
# -*- coding:utf-8 -*-

###
# ch2 perception
# 判别模型，线性，多解
# 多解依赖于初值的选择和过程中随机误分类点的选择
# data: Iris data ./data/iris.data.txt
#       url: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# loss func: 误分类点到超平面距离之和
# optimizer: 随机梯度下降
# 模型终止：直到没有误分类的点
# 模型学习：超参数wight，bais
###

import numpy as np
import matplotlib
import pandas as pd
import tensorflow as tf
from LoadHelper import *

learningRate = 0.01
trainPath = "./data/iris.data.csv"

# type: train, dev, test
# path: data file path
def loadData(type, path):
    x,y = pythonlibLoad(path)
    x1 = x[0:99:5,0:2]
    print(x1)
    y1 = y[0:99:5]

    y1 = list(map(renamelabel,y1))
    print(y1)
    x1 = np.array(x1)
    y1 = np.array(y1)
    return x1,y1

def renamelabel(l):
    return {
        2:-1,
        1: 1
    }.get(l,-1)

# 基于随机梯度下降 + 所选误分类点到超平面的距离
# 超平面：kw+b
def lossFunc(x, k, b):
    return 0

'''f(x) = sign(wx+b)'''
def perception(w, b, learnRate): # TODO parameter that can be used to different np.array.shape
    x,y = loadData("train",trainPath)
    hasWrong=True
    while(hasWrong):
        # TODO how rand choose wrong point
        rundomcount=20
        rundomtry=0
        while(rundomtry < rundomcount):
            r = np.random.randint(0,20,1,dtype='int')
            if (w.T.dot(x[r])+b)*y[r] < 0:
                w = w + learningRate*y[r]*x[r]
                b = b + learningRate*y[r]
                break
            else:
                rundomtry+=1
        if(rundomtry >= rundomcount):
            for i in range(y.shape[0]):
                if (w.T.dot(x[r]) + b) * y[r] < 0:
                    w = w + learningRate * y[r] * x[r]
                    b = b + learningRate * y[r]
                    break
            if i >= y.shape[0]:
                hasWrong = False
        else:
            continue


if __name__ == "__main__":
    w=np.array([0,0]) #超参数初值
    b=0
    perception(w,b, learningRate)

