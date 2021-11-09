import pandas as pd
import numpy as np
from sklearn import preprocessing

# Normalization dataset to [0,1]
def normalization(list):
	dataset=np.array(list)
	min_max_scaler=preprocessing.MinMaxScaler()
	
	normaldataset=min_max_scaler.fit_transform(dataset)
	return normaldataset

# Load S1 dataset
dataset = pd.read_csv('../dataset/Lifesci.csv', header = None, sep=r'\s*,\s*', na_values="?", engine='python')
normaldata = normalization(dataset)
savefile = pd.DataFrame(normaldata)
savefile.to_csv('../dataset/Lifesci_normal.csv', index = False, header = None)