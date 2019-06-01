# -*- encoding: utf-8 -*-
'''
@Author  :   Xuesong TU
@File    :   k_means.py    
@Contact :   xuesong.mac@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Time    :   2019/6/1 11:15
@Description :
_____________________________________________________________
'''

import matplotlib.pyplot as plt
import numpy as np


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def k_means():
    return 0


if __name__ == "__main__":
    mean = [90, 30]
    cov = [[3, 0], [0, 3]]
    x, y = np.random.multivariate_normal(mean, cov, 500).T
    plt.plot(x, y, '.')
    plt.axis('equal')
    plt.show()