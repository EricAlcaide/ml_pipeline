import numpy as np 
import pandas as pd 

def clean_3_lines(filename):
	with open(filename, 'r') as fin:
		data = fin.read().splitlines(True)
	with open(filename, 'w') as fout:
		fout.writelines(data[3:])

	return True

def clean_columns(filename, destin, col1=4, col2=7):
	data = pd.read_csv(filename, delimiter="\t")
	clean = data.iloc[:, 4:7]
	clean.to_csv(destin, sep=",", header=["ecg", "eda", "acc"])
	return True



