from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
import pandas as pd 
import numpy as np

from model import Model
# fix random seed for reproducibility
np.random.seed(7)

filename = "sample.txt"
destin = "processed.txt"
model_file = "model.h5"

# First get raw chunk. Delete lines and columns
x = [] # ecg, mean_eda, mean_acc, maxmin_eda, maxmin_acc

# Predict data
network = Model(model_file)
result = network.predict(np.array([x]))

print(result)

result[result > 0.75] = 1
result[result <= 0.75] = 0
# Es un array 1 element
print(result)