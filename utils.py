def get_data(filename):
	return np.genfromtxt(filename, delimiter=',').astype(float)[1:]

def train_test(data, part=0.7):
	split = int(len(data)*0.7)
	print(split, len(data))
	train, test = data[:split], data[split:]
	# x,y split
	x_train, y_train = train[:, 1:], train[:, 0]
	x_test, y_test = test[:, 1:], test[:, 0]

	return x_train, y_train, x_test, y_test

data = get_data("data/final_data.txt")