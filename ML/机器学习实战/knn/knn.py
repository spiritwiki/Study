#-*- coding:utf8 -*-
"""
机器学习算法之KNN
"""

from numpy import *
import collections

def classify(in_, datas, labels, k):
    """
    分类
    in_: 待分析数据; datas: 训练集; labels: 训练集标签; k: 近邻个数;
    """
    data_size = datas.sharp[0]
    diff_mat = tile(in_, (data_size, 1)) - datas
    sq_diff_mat = diff_mat ** 2
    sq_distance = sq_diff_mat.sum(axis = 1)
    distance = sq_distance ** 0.5
    sorted_distance = distace.argsort()
    vote_labels = (labels[sorted_distance[i]] for i in range(k))
    label_counts = collections.Counter(vote_labels)
    return label_counts.most_common(1)[0]
    
    
