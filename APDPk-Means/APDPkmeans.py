'''
Description: 
Autor: Jechin
Date: 2021-11-08 15:26:03
LastEditors: Jechin
LastEditTime: 2021-11-09 18:00:36
'''
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class APDPkmeans(object):
    def __init__(self, data, n_clusters, eps = 10, iters_max = 10):
        self.data = data
        self.n_sample, self.dimensional = data.shape
        self.sensitivity = self.dimensional + 1
        self.k = n_clusters
        self.totaleps = eps
        self.iters = iters_max
        self.generate_eps()
        
    def l2_distance(self, datapoint):
        dists = np.sqrt(np.sum((self.centers - datapoint)**2, axis=1))
        return dists
    
    def init_center(self):
        block=int(self.n_sample/self.k)
        x = 0
        list=np.zeros([self.k,self.data.shape[1]])
        for i in range(self.k):
            list[i:]=self.data[random.randint(x, x + block)]
            x=x+block
        center_array=list
        return center_array
    
    def mineps(self, k, N, d):
        minepslion=np.sqrt(((500*k**3)/N**2)*np.power((d+(4*d*0.45**2)**(1/3)),3))
        result=round(minepslion,3)
        return result

    def generate_eps(self):
        print("total_eps = ", self.totaleps)
        mineps = self.mineps(self.k, self.n_sample, self.dimensional)
        t = int(self.totaleps/mineps)
        if t > self.iters:
            d = (2*self.totaleps-2*mineps*self.iters)/(self.iters*(self.iters-1))
            eps = np.zeros(self.iters)
            for n in range(self.iters):
                e = mineps+n*d
                eps[n] = e
            self.eacheps = eps[::-1]
            print("AP: ", eps[::-1])
        else:
            eps = np.full(self.iters, self.totaleps / self.iters)
            print("Uniform: ", eps)
            self.eacheps = eps

    def classify(self, datapoint):
        """
        Given a datapoint, compute the cluster closest to the
        datapoint. Return the cluster ID of that cluster.
        """
        dists = self.l2_distance(datapoint)
        return np.argmin(dists)

    # laplace_array
    def laplacenoise_array(sensitivity,epslion,len,num):  #  产生laplace噪声数组,len是维数，num是生成的个数
        location=0
        scale=sensitivity/epslion
        list=[]
        for i in range(num):
            list .append( np.random.laplace(location, scale, len))
            Laplacian_noise=np.array(list)
        return Laplacian_noise
    
    def fit(self, show = True):
        '''
        description: 
        param {show: if show sse each iter}
        return {clusters, sse}
        author: Jechin
        '''
        self.initial_centers = self.init_center()
        self.centers = np.copy(self.initial_centers)
        self.sse = []
        old_assigns = None
        n_iters = 0
        
        while True:
            new_assigns = [self.classify(datapoint) for datapoint in self.data]
            
            if new_assigns == old_assigns or n_iters == self.iters:
                print(f"Training finished after {n_iters} iterations!")
                self.end_iter = n_iters
                break
                
            old_assigns = new_assigns
            epsilon = self.eacheps[n_iters]
            n_iters += 1
            sse = 0
            laplace_noise = []
            for _ in range(self.dimensional):
                laplace_noise.append(np.random.laplace(0, self.sensitivity / epsilon, self.k))
            
            laplace_num = np.random.laplace(0, self.sensitivity / epsilon, self.k)
            laplace_sumx = np.random.laplace(0, self.sensitivity / epsilon, self.k)
            laplace_sumy = np.random.laplace(0, self.sensitivity / epsilon, self.k)
            centers = np.copy(self.centers)
            
            if show:
                print(f"---------------------------------\n{n_iters} iter: eps = ", epsilon)
            
            # recalculate centers
            for id_ in range(self.k):
                points_idx = np.where(np.array(new_assigns) == id_)
                datapoints = self.data[points_idx]
                num = len(datapoints) + laplace_num[id_]
                # sumpoints = datapoints.sum(axis = 0) + np.array([laplace_sumx[id_], laplace_sumy[id_]])
                sumpoints = datapoints.sum(axis = 0) + np.array([laplace[id_] for laplace in laplace_noise])
                centers[id_] = sumpoints / num
                sse += np.sqrt(np.sum((datapoints - self.centers[id_])**2, axis=1)).sum()
            
            self.centers = np.copy(centers)
            self.sse.append(sse)
            
        self.clusters = np.array([self.classify(datapoint) for datapoint in self.data])
        sse = self.sse[n_iters - 1]
        return self.clusters, sse
            
    def plot_clusters_sse(self):
        if self.dimensional != 2:
            print("Hints: only 2-dimensional data can be show clusters in gragh.")
        else:
            plt.figure(figsize=(12,10))
            plt.title("APDPk-means cluster")
            plt.scatter(self.data[:, 0], self.data[:, 1], marker='.', c=self.clusters)
            plt.scatter(self.centers[:, 0], self.centers[:,1], c='r')
            plt.plot()
        
        sse_x_label = range(self.end_iter)
        plt.figure(figsize=(12,10))
        plt.title("APDPk-means sse")
        plt.plot(sse_x_label, self.sse, marker='o')
        plt.show()