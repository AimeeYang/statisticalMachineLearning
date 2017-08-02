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
import math

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


def get_mid(curdata, axis_no):
    cnt = curdata.shape[0]
    tmpdata =  curdata[:,axis_no]
    sorteddata = sorted(tmpdata)
    return sorteddata[math.floor(cnt/2)]

'''
:parameter childname = "Left"/"Right"
'''
def buildKD(remain_data, axis_no, parent, childname):
    if (remain_data == None) or (remain_data.shape[0] == 0):
        return

    # build remain_data
    remain_less_data=[]
    remain_more_data=[]
    node = {}   # TODO whether use class/struct

    mid = get_mid(remain_data,axis_no)
    node["mid"] = mid
    node["axis"] = axis_no
    node["parent"] = parent
    for d in remain_data:
        if d[axis_no] < mid:
            remain_less_data.append(d)
        elif d[axis_no] > mid:
            remain_more_data.append(d)
        else:
            if "data" in node.keys():
                node["data"].append(d)
            else:
                node["data"] = []
                node["data"].append(d)

    axescnt = remain_data.shape[1]
    new_axis_no = (axis_no + 1)%axescnt
    buildKD(np.array(remain_less_data), new_axis_no, node, "Left")
    buildKD(np.array(remain_more_data), new_axis_no, node, "Right")

    if parent is None:
        return node     # 返回构建好的kd树的根节点
    else:
        if childname == "Left":
            parent["Left"] = node
        else:
            parent["Right"] = node

def searchKDFindNode(root, target):
    # down find target belong to which leave

    if root["mid"] == target[root["axis"]]:
        return root
    elif root["mid"] < target[root["axis"]]:
        if "Left" in root.keys:
            searchKDFindNode(root["Left"],target)
        else:
            return root
    else:
        if "Right" in root.keys:
            searchKDFindNode(root["Right"],target)
        else:
            return root

'''
check curnode's parent's other child, namely curnode's brother
'''
def isBrotherIntersect(target, curnode, kneighbour, p, k):
    # TODO make sure here is the minumum or the k-th neighbour
    minimumNeighbour = kneighbour[k-1] # suppose kneighbour is sorted list and with asc order
    r = distance(p,minimumNeighbour, target)
    mid_of_curnode_and_brother = curnode["parent"]["mid"]
    parent_axis = curnode["parent"]["axis"]
    return math.fabs(target[parent_axis] - mid_of_curnode_and_brother) <= r

def buildKNeighbourByAList(data, kneighbour,target, k, p):
    if kneighbour is None:
        kneighbour = []
    for d in data:
        dis = distance(p, d, target)
        if len(kneighbour) < k:
            kneighbour.append({"data": d,
                               "dist": dis})
        else:
            sorted_kneighbour = OrderedDict(sorted(kneighbour.items(), key=lambda t: t[1]))
            if dis < sorted_kneighbour[k-1]["dist"]:
                kneighbour.pop(k-1)
                kneighbour.append({"data": d,
                                   "dist": dis})
    return kneighbour

def upAndDownSearch(node, kneighbour, target, p, k):
    if kneighbour is None:
        kneighbour = []

    # search node's data
    kneighbour =buildKNeighbourByAList(node["data"], kneighbour, target, k, p)

    # search parent node's data
    if "parent" in node.keys and node["parent"] != None :
        parent = node["parent"]
        kneighbour = buildKNeighbourByAList(parent["data"], kneighbour, target, k, p)
        # check if intersect with node's brother
        if isBrotherIntersect(target, node, kneighbour,p, k):
            if node["mid"] < parent["mid"]:
                kneighbour = downSearch(parent["Right"], kneighbour, target, p, k)
            else: # here children's mid must not equal to parent's mid
                kneighbour = downSearch(parent["Left"], kneighbour, target, p, k)

    return kneighbour

def isBrotherChildrenIntersect(target, brother, childtype, kneighbour, p, k):
    brothermid = brother["mid"]
    brotheraxis = brother["axis"]
    # TODO make sure here is the minumum or the k-th neighbour
    minimumNeighbour = kneighbour[k - 1]  # suppose kneighbour is sorted list and with asc order
    r = distance(p, minimumNeighbour, target)
    parent = brother["parent"]
    parentmid = parent["mid"]
    if(childtype == "Left" and target[brotheraxis] < brothermid) or (childtype == "Right" and target[brotheraxis] > brothermid):
        return math.fabs(target[parent["mid"]] - parentmid) <= r
    else:
        parentbrotherdot = [0,0]
        if parent["axis"] > brotheraxis :
            parentbrotherdot = np.array([brothermid, parentmid])
        else:
            parentbrotherdot = np.array([parentmid, brothermid])   # TODO multidimension how get the 交点
        dis_neighbour_dot = distance(p, target, parentbrotherdot)
        return dis_neighbour_dot <= r


def downSearch(node, kneighbour, target, p, k):
    # search node's data
    kneighbour = buildKNeighbourByAList(node["data"], kneighbour, target, k, p)

    # search node's Left child
    if "Left" in node.keys and isBrotherChildrenIntersect(target, node, "Left", kneighbour, p, k):
        kneighbour = downSearch(node["Left"], kneighbour, target, p, k)

    # search node's Right child
    if "Right" in node.keys and isBrotherChildrenIntersect(target, node, "Right", kneighbour, p, k):
        kneighbour = downSearch(node["Right"], kneighbour, target, p, k)

    return kneighbour

def getKNNBasedOnKDTree(root, target, k, p):
    node = searchKDFindNode(root, target)
    # 1. up till root find the nearest neighbour? TODO check if need till root? any optimize
    # 2 node's brother check by circle cross, if cross, then, recursive search brother and its childern.
    #   TODO CHECK what is the end point, lefe or any optimize

    # Here up to root, and if down, till leave
    # TODO 圆与区域相交的判别方法  target与各节点的mid值 的距离 与 圆的半径比较 <= 则相交
    kneighbour = upAndDownSearch(node, None, target, p, k)

    # TODO 多数表决

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

'''
:parameter p: p - distance
'''
def kdBasedKNN(x_test, x_train, y_train, k, p):
    root = buildKD(x_train,0, None, "")
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

    #y_test_pre = normalKNN(x_test, x_train, y_train, k, p) # TODO ACCURACY

    # #test data for kd tree build
    # x_train=np.array([[2,3],
    #          [5,4],
    #          [9,6],
    #          [4,7],
    #          [8,1],
    #          [7,2]])
    y_test_pre2 = kdBasedKNN(x_test, x_train, y_train, k, p)

