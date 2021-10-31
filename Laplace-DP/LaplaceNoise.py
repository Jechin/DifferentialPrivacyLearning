'''
Description: Laplace-DP
Autor: Jechin
Date: 2021-10-31 10:07:20
LastEditors: Jechin
LastEditTime: 2021-11-01 01:13:26
Dataset: adults
Epsilon: 0.125
TypeOfQuery: Histogram Queries
'''

import pandas as pd
import numpy as np
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

# Set parameters for Laplace function implementation
# l1 sensitivity = 1
# epsilon = 0.125
location = 0.0
scale = 1.0/0.125 

# Gets random laplacian noise for all values
Laplacian_noise = np.random.laplace(location, scale, len(datacount))
print("Laplacian_noise:\n", Laplacian_noise)

# Add random noise generated from Laplace function to actual count
noisydata = datacount + Laplacian_noise
print("noisydata:\n", noisydata)

# Get index of datacount, "age"
index=list(datacount.index)
# Transfer type of Laplace Noise from 'numpy.ndarray' to 'pandas.core.series.Series' and index
laplacenoise=pd.Series(Laplacian_noise,index=index)

# Generate noisydata histogram
plt.figure("Figure 1: Laplace noisydata histogram")
plt.title("Laplace noisydata histogram")
noisydata.plot(kind="bar",color = 'g')
plt.savefig("Laplace-DP/Noise Data.png")


# Generate actual and noise histogram
plt.figure("Figure 2: Laplace actual and noise histogram")
plt.ylabel("num")
plt.xlabel("age")
plt.bar(range(len(noisydata)),datacount,label='datacount',fc='y')
plt.bar(range(len(noisydata)),laplacenoise,bottom=datacount,label='noise',tick_label=index,fc='r')
plt.title("Laplace actual and noise histogram")
plt.legend()
plt.plot()
plt.savefig("Laplace-DP/Actual and Noise.png")
plt.show()