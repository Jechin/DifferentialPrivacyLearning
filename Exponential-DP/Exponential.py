'''
Description: Exponential Mechanism in DP
Autor: Jechin
Date: 2021-10-31 23:59:37
LastEditors: Jechin
LastEditTime: 2021-11-01 00:56:55
Dataset: adults
Epsilon: 0, 0.01, 0.05
TypeOfQuery: Non-numeric Queries
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
datacount = dataset["Country"].value_counts()
print("datacount: \n", datacount)
print("------------------------------------------")

# Get index of datacount, "Country"
index = list(datacount.index)

# Get value of datacount, "number each Country"
number = list(datacount.values)

# Set parameters for Exponential function implementation
# L1 Sentivity = 1
# Epsilon =  0, 0.01, 0.05
eps = [0.0, 0.01, 0.05]
sensitivity = 1.0

# Write dateset to excel
writer = pd.ExcelWriter('Exponential-DP/results.xlsx')
header = ["Values"]
datacount.to_excel(excel_writer=writer, sheet_name="sheet1", header=header)

for i in range(3):
    # Calculate Score with Exponential Mechanism
    score = np.exp(eps[i] * datacount / (2 * sensitivity))
    print("\nscore: \n", score)
    print("------------------------------------------")

    # Calculate probablity of each country
    sum_score = score.sum()
    probablity = score / sum_score
    print("\nprobablity: \n", probablity)
    print("------------------------------------------")

    # Write probablity to excel
    label = "eps=" + str(eps[i])
    header = []
    header.append(label)
    probablity.to_excel(excel_writer=writer, sheet_name="sheet1", startcol=i + 2, index=False, header=header)

writer.save()    
writer.close()
