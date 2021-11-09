'''
Description: 
Autor: Jechin
Date: 2021-11-08 23:28:09
LastEditors: Jechin
LastEditTime: 2021-11-08 23:45:28
'''

import numpy as np

def fmeasure(x_true, y_pred, n_sample, k_clusters):
    x_true_process = []
    y_pred_precess = []
    for id_ in range(k_clusters):
        x_true_process.append(np.where(np.array(x_true) == id_)[0])
        y_pred_precess.append(np.where(np.array(y_pred) == id_)[0])

    f_measure = 0.0

    for x in range(k_clusters):
        f1_scores = np.array([0]*k_clusters)
        for y in range(k_clusters):
            n_ij = np.intersect1d(x_true_process[x], y_pred_precess[y]).size
            if n_ij :
                recall = n_ij / x_true_process[x].size
                precision = n_ij / y_pred_precess[y].size
                f1_scores = np.append(f1_scores, 2 * recall * precision/(recall + precision))
        
        f1 = f1_scores[np.argmax(f1_scores)]
        f_measure += x_true_process[x].size / n_sample * f1
    
    return f_measure
