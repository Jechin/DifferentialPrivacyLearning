'''
Description: Gaussian Differential Privacy
Autor: Jechin
Date: 2021-10-31 20:21:39
LastEditors: Jechin
LastEditTime: 2021-11-01 01:12:49
Dataset: adults
Epsilon: 0.125
Delta: 10^(-5)
TypeOfQuery: Histogram Queries
'''


import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Load Adult dataset
dataset = pd.read_csv("dataset/adult.data.txt",
    names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],sep=r'\s*,\s*',na_values="?")
dataset.tail()

#Find actual data count
datacount = dataset["Age"].value_counts()
print("datacount:\n", datacount)

# Set parameters for Gaussian function implementation
# l2 sensitivity = 1
# epsilon = 0.125
# delta = 0.00001
location = 0.0
scale = np.sqrt(2.0*np.log(1.25/0.00001))*(1.0/0.125)

# Gets random Guassian noise for all values
Gaussian_noise = norm.rvs(location, scale, len(datacount))
print("Gaussian_noise:\n", Gaussian_noise)

# Add random noise generated from Gaussian function to actual count
noisydata = datacount + Gaussian_noise
print("noisydata:\n", noisydata)

# Get index of datacount, "age"
index=list(datacount.index)
# Transfer type of Laplace Noise from 'numpy.ndarray' to 'pandas.core.series.Series' and index
Gaussiannoise=pd.Series(Gaussian_noise,index=index)

# Generate noisydata histogram
plt.figure("Figure 1: Gaussian noisydata histogram")
plt.title("Gaussian noisydata histogram")
noisydata.plot(kind="bar",color = 'g')
plt.savefig("Gaussian-DP/Noise Data.png")

# Generate actual and noise histogram
plt.figure("Figure 2: Gaussian actual and noise histogram")
plt.ylabel("num")
plt.xlabel("age")
plt.bar(range(len(noisydata)),datacount,label='datacount',fc='y')
plt.bar(range(len(noisydata)),Gaussiannoise,bottom=datacount,label='noise',tick_label=index,fc='r')
plt.title("Gaussian actual and noise histogram")
plt.legend()
plt.plot()
plt.savefig("Gaussian-DP/Actual and Noise.png")
plt.show()