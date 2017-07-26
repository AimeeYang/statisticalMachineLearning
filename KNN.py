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
import operator
from collections import OrderedDict

def loadData(filePath):
    x, y = numpyLoad(filePath)
    # for calculate simply, use the first column
    x = x[:, :2]
    print("x: ")
    print(x)
    print("y: ")
    print(y)
    return x,y

'''
    :parameter p p距离
    :parameter x1,x2 求x1,x2两点距离
'''
def distance(p,x1,x2):
    dist=0
    if p == 2:
        # (x1-x2)**2 return 每个坐标的平方
        print((x1-x2)**2)
        print(np.array((x1-x2)**2).flat)
        print(np.sum(np.array((x1-x2)**2).flat))
        print(np.sqrt(np.sum(np.array((x1-x2)**2).flat)))
        return np.sqrt(np.sum(np.array((x1-x2)**2).flat))
    return None

def buildKD(x_train):
    axescnt = x_train.shape[]
    return None

def searchKD():
    return None

#TODO try array sort desc
###
# k neighbour store in stack(大根堆)
# if not k not much, maybe using normal sorted list/array is more efficency
###
def normalKNN(x_test, x_train, y_train, k, p):
    y_test_pre = []
    for i in range(x_test.shape[0]):
        #y_tmp = np.empty((1,2)) #[] # maintain y_tmp be a sorted map: asc
        y_tmp = {}

        for j in range(x_train.shape[0]):
            tmp_dist = distance(p, x_test[i],x_train[j])
            if len(y_tmp) < k:
                # y_tmp = np.append(y_tmp,[[tmp_dist,j]],axis=0) #y_tmp.append([tmp_dist, j])
                # y_tmp = np.sort(y_tmp, axis=0) # sort along the first axis

                #y_tmp[tmp_dist] = j # 这里存在问题 key的值不唯一
                y_tmp[j] = tmp_dist
                # # map sort by key
                # y_tmp = OrderedDict(sorted(y_tmp.items(), key=lambda t: t[0]))
                # # <=> y_tmp = OrderedDict(sorted(y_tmp.items()))
                # map sort by value
                y_tmp = OrderedDict(sorted(y_tmp.items(), key=lambda t: t[1]))
                # # map sort by key length
                # y_tmp = OrderedDict(sorted(y_tmp.items(), key=lambda t: len(t[0])))
                print("y_tmp")
                print(y_tmp)
            else:
                if tmp_dist < y_tmp.values()[k-1]:
                    y_tmp.pop(y_tmp.keys()[k-1])
                    y_tmp[j] = tmp_dist
                    y_tmp = OrderedDict(sorted(y_tmp.items(), key=lambda t: t[1]))

        # 多数表决
        y_label_tmp = {}
        for n in range(k):
            curlabel = y_train[y_tmp.keys()[n]]
            if len(y_label_tmp) == 0:
                y_label_tmp[curlabel] = 1
            else:
                if y_label_tmp.has_key(curlabel):
                    y_label_tmp[curlabel] = y_label_tmp[curlabel] + 1
                else:
                    y_label_tmp[curlabel] = 1
        y_label_tmp_sorted = sorted(y_label_tmp.items(), key=operator.itemgetter(1)) # may sorted by values

        y_test_pre.append(y_label_tmp_sorted.pop()[0])


    y_test_pre = np.array(y_test_pre)
    return y_test_pre

def kdBasedKNN():
    return None

if __name__ == "__main__":
    # init para
    filePath = "./data/iris.data.txt"
    k = 4
    p = 2
    x, y = loadData(filePath)
    # TODO cross validation
    # here just split by the data rule 50,50,50 => each label get 10 value as test
    x_test = np.vstack((x[:10],x[50:60],x[100:110]))
    y_test = np.vstack((y[:10],y[50:60],y[100:110]))
    # print(x_test)
    print(x_test.shape)
    # print(y_test)
    print(y_test.shape)
    x_train = np.vstack((x[10:50],x[60:100],x[110:150]))
    print(x_train.shape)
    # print(x_train)
    y_train = np.vstack((y[10:50],y[60:100],y[110:150]))

    y_test_pre = normalKNN(x_test, x_train, y_train, k, p)

