from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
import numpy as np
# fix random seed for reproducibility
np.random.seed(7)

class Model():
	def __init__(self, filename="model.h5"):
		self.nn = load_model(filename)

	def predict(self, x):
		# X must be 5 dimensional:
		# ppm, mean_eda, mean_acc, maxmin_eda, maxmin_acc )
		return self.nn.predict(x)
