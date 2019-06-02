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


def get_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def get_centroids(points):
    x = 0
    y = 0
    for i in points:
        x += i[0]
        y += i[1]

    return [x/len(points), y/len(points)]


def get_argmin_index(l):
    min = l[0]
    index = 0
    for i in range(1, len(l)):
        if l[i] < min:
            min = l[i]
            index = i

    return index


def k_means(points, n, k):
    clusters = [[] for i in range(k)]
    centroids = []

    # generate k centroids randomly
    for i in range(4):
        centroids.append(np.random.rand(2) * 50)


    # clustering the points accroding to the centroids
    for i in range(n):
        distances = []
        for j in range(k):
            distances.append(get_distance(points[i], centroids[j]))

        index = get_argmin_index(distances)
        clusters[index].append(points[i])

    # update the centroids

    for i in range(k):
        centroids[i] = get_centroids(clusters[i])

    print(centroids)
    print(clusters)


if __name__ == "__main__":
    mean1 = [90, 30]
    cov1 = [[16, 0], [0, 15]]
    x1, y1 = np.random.multivariate_normal(mean1, cov1, 300).T

    mean2 = [80, 60]
    cov2 = [[12, 0], [0, 14]]
    x2, y2 = np.random.multivariate_normal(mean2, cov2, 500).T

    mean3 = [20, 40]
    cov3 = [[13, 0], [0, 13]]
    x3, y3 = np.random.multivariate_normal(mean3, cov3, 400).T

    mean4 = [50, 60]
    cov4 = [[20, 0], [0, 20]]
    x4, y4 = np.random.multivariate_normal(mean4, cov4, 400).T

    x = np.concatenate((x1, x2, x3, x4), axis=0)
    y = np.concatenate((y1, y2, y3, y4), axis=0)

    points = []
    for i in range(1600):
        points.append((x[i], y[i]))

    k_means(points, 1600, 4)
    plt.plot(x, y, '.', markersize=2)
    plt.axis('equal')
    plt.show()
