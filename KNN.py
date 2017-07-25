#!/usr/bin/python
# -*- coding:utf-8 -*-

###
# CH3 KNN
# 没有直观的学习过程
# 3要素：k的选择，距离算法选择，表决选择
#   k的选择：一般选择较小k值
#       k值 vs 分类个数：二者是不同的概念
#   距离算法：一般的p距离
#   表决算法：TODO MAKE SURE 一般的多数表决法？
# 为了提高搜素速度：采用特殊的存储结构，如kd树
#
###

import numpy as np
import matplotlib.pyplot as plt
from LoadHelper import *

def loadData(filePath):
    x, y = numpyLoad(filePath)
    # for calculate simply, use the first column
    x = x[:, :2]
    print("x: ")
    print(x)
    print("y: ")
    print(y)
    return x,y

def distance():
    return None

def buildKD():
    return None

def searchKD():
    return None

###
# k neighbour store in stack(大根堆)
# if not k not much, maybe using normal sorted list/array is more efficency
###
def normalKNN():
    return None

def kdBasedKNN():
    return None

if __name__ == "__main__":
    filePath = "./data/iris.data.txt"
    x, y = loadData(filePath)
