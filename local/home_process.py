import numpy as np 
import pandas as pd
import os
# Import preprocess functions
from chunk_150_best import *

origin = "data.txt"
destin = "sample.txt"

# execute data gathering
# os.system("""python bitalino_hack.py /dev/tty.BITalino-39-96-DevB 10 "2;3;5" 100 10 ./"""+origin)


# preprocess data
with open(origin, 'r') as fin:
	data = fin.read().splitlines(True)

dataset = [[], [], []]
for row in data:
	i, val = row.split(";")
	dataset[int(i)].append(float(val))

dataset = np.array(dataset).T 
frame = pd.DataFrame(dataset)
frame.to_csv(destin, sep=",", header=["ecg", "eda", "acc"])

x = sum_up(destin, label=9)[1:]
print(x)
# execute data gathering
os.system("""curl -H "Content-Type: application/json" -X POST http://167.99.74.49/messages -d 
		  '{"name": "Ignasi", "ecg": x[0], "mean_eda": x[1], "mean_acc": x[2], "maxmin_eda": x[3], "maxmin_acc": x[4]}' """)