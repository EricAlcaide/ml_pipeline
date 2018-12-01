from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
import pandas as pd 
import numpy as np

from model import Model
from chunk_150_raw import *
from chunk_150_best import *
# fix random seed for reproducibility
np.random.seed(7)

filename = ""
destin = "processed.txt"
model_file = "model.h5"

# First get raw chunk. Delete lines and columns
clean_3_lines(filename)
clean_columns(filename, destin, col1=4, col2=7)

# Process data
x = sum_up(destin, label=9)[1:]

# Predict data
network = Model(model_file)
result = network.predict(np.array([x]))

print(result)