import numpy as np 

def get_data(file):
	return np.genfromtxt(file, delimiter=',').astype(float)[1:].T[1:]

def center_hr(data):
	# Change mean values and std to a reference
    return (data-np.mean(data))/np.std(data)

def mean(data, periods=3.0):
    new = []
    for i,e in enumerate(data):
        if i>periods:
            new.append(np.sum(data[int(i-periods):i])/periods)
    return np.array(new)

def heart_rate(data):
    time = len(data)/15
    spikes = 0
    allow = True
    for d in data:
        if d>1:
            if allow == True: 
                spikes += 1
                allow = False
                # print(spikes)
        else:
            if allow == False: allow = True
       
    return spikes/float(time) * 60

def max_min(data):
    return np.amax(data)-np.amin(data)

# Sample procedure: get_data - center - mean - feature (heart_rate, minmaxes)
# ppm, media eda, media acc, max-min eda, max-min acc
def sum_up(filename, label=9):
	# get data and smooth it
	data = get_data(filename)
	data_mean = [mean(d) for d in data]
	# get measures
	hr = heart_rate(center_hr(data_mean[0]))
	mean_eda = np.mean(data_mean[1]) 	# - param of reference
	mean_acc = np.mean(data_mean[-1]) 	# - param of reference
	maxmin_eda = max_min(data_mean[1])
	maxmin_acc = max_min(data_mean[2])
	# Sum it up
	measures = np.array([label, (hr-90)/10, (mean_eda-9)/1.5, mean_acc*5, maxmin_eda, maxmin_acc])
	return measures