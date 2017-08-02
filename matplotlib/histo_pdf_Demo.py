#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
2-d demo of matplotlib. 
    In this demo, show the way to draw common pdf picture, and histogram picture.
  PDF is short for 概率分布函数
    I. pdf: 分为以下几类：
        1. 根据分布函数
        2. 特殊？？ 
Reference:

'''

import numpy as np
import matplotlib.pyplot as plt


# TODO Check if exist 需特殊方法绘制的PDF
def drawPDFByFormular(x, formular, pdfName, sigma, mu):
    # y = yield formular(x0,sigma, mu) for x0 in x #TODO HOW IMPLEMENTATION THIS
    plt.plot(x, y, 'r-', label=pdfName)
    # plt.grid()
    plt.show()

def normalDistribution(x, sigma, mu):
    return np.exp(-((x-mu)**2)/2*sigma**2) / (np.sqrt(2*np.pi) * sigma)

def histo(x):
    x = np.random.rand(10)
    # t = np.arange(len(x))
    # n, bins, pathes = plt.hist(x, 30, color='m', alpha=0.5)

    #n, bins, pathes = plt.hist(x)
    # TODO draw plt picture and the x vaule is the same with the real value
    n, bins, pathes = plt.hist(x, 10) # ValueError: `bins` should be a positive integer.
    print("n: ")
    print(n)                # 值为输入的x  [ 2.  0.  0.  1.  1.  2.  0.  0.  2.  2.]
    print("bins")
    print(bins)             # 值为自动划分的x区间点： [ 0.0563891   0.14445995  0.2325308   0.32060165  0.4086725   0.49674335
                            # 0.5848142   0.67288505  0.7609559   0.84902675  0.9370976 ]
    print("pathes: ")
    print(pathes)
    plt.show()

    return None

if __name__ == "__main__":
    print("test plt draw histo picture")
    histo(None)