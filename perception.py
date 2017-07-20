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
    x1 = np.array(x1).astype(np.float) # 转str类型的array为float类型的array
    print(x1)
    y1 = y[0:99:5]

    y1 = list(map(renamelabel,y1))
    print(y1)

    y1 = np.array(y1) # TODO 此处的y1.shape 为什么不是 int 1 而是 tuple (1,)? 是否因为shape的类型是tuple的
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
    recursivetime =0
    while(hasWrong):
        # TODO how rand choose wrong point
        recursivetime += 1
        print("===== recursivetime: "+str(recursivetime))
        randomcount=20
        randomtry=0
        while(randomtry < randomcount):
            print("randomtry: "+str(randomtry)+", b: "+str(b)+", w: ")
            print(w)
            r = np.random.randint(0,20,1,dtype='int')[0]
            # 下面注意dtype 避免出现str类型的array;
            #   否则回报 错误：ValueError: data type must provide an itemsize
            print("w.dot(x[r].T)+b)*y[r]: " +str((w.dot(x[r].T)+b)*y[r]))
            if (w.dot(x[r].T)+b)*y[r] <= 0:   # 此处<=0
                w = w + learningRate*y[r]*x[r]
                b = b + learningRate*y[r]
                break
            else:
                randomtry+=1
        if(randomtry >= randomcount):
            for i in range(y.shape[0]):
                print("i: "+str(i))
                if (w.dot(x[r].T) + b) * y[r] <= 0:
                    w = w + learningRate * y[r] * x[r]
                    b = b + learningRate * y[r]
                    break
            if i >= y.shape[0]-1:
                hasWrong = False
                print("TOTAL END *****************")
        else:
            continue

    print("b: " + str(b) + ", w: ")
    print(w)
    return w,b


if __name__ == "__main__":
    w=np.array([0,0]) #超参数初值
    b=0
    # TODO draw the process of hyperplane with plt, dynamic & result
    w1, b1 = perception(w,b, learningRate)
    print("b1: "+str(b1)+", w1: ")
    print(w1)

