import numpy as np 
import pandas as pd 

def clean_3_lines(filename, destin):
	with open(filename, 'r') as fin:
		data = fin.read().splitlines(True)
	with open(destin, 'w') as fout:
		# fout.write()
		fout.writelines(data[3:])

	return True

def clean_columns(filename, destin, col1=4, col2=7):
	data = pd.read_csv(destin, delimiter="\t", header=None)
	clean = data.iloc[:, col1:col2]
	clean.to_csv(destin, sep=",", header=["ecg", "eda", "acc"])
	return True



