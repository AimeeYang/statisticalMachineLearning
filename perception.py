#!/usr/bin/python
# -*- coding:utf-8 -*-

###
# ch2 perception
# 判别模型，线性，多解 TODO 补解依赖
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

learningRate = 0.001
trainPath = "./data/iris.data.txt"

# type: train, dev, test
# path: data file path
def loadData(type,path):
    return 0

def lossFunc():
    return 0

def perception(): # TODO parameter that can be used to different np.array.shape
    data = loadData("train",trainPath)



