from bitalino import BITalino
import time
import serial
import sys
import os

if len(sys.argv) != 7:
	print("USAGE: python example1.py {/dev/port_to_bitalino|COMx} {running_time [s] } {acq_channels} {sampling_rate} {nSamples} {path_to_file}")
	print("EXAMPLE: python example1.py COM3 10 \"1;2;3\" 1000 10 c:\\path\to\file\bitalino.txt")
	print("EXAMPLE: python example1.py /dev/ttyBITalino 10 \"1;2;3\" 1000 10 ~/data/bitalino.txt")
	print("The example will open the COM3 port, run for 10 seconds, sample the channels 1, 2 and 3 using a Sample Frequency of 1 KHz and 10 samples per channel, it will save the data to the bitlino.txt file.")
	sys.exit(0);

macAddress = sys.argv[1]
running_time = int(sys.argv[2])
    
#batteryThreshold = 30
#batteryThreshold = 30
acqChannels = map(int,sys.argv[3].split(';'))
print(acqChannels)
samplingRate = int(sys.argv[4])
nSamples = int(sys.argv[5])
path = sys.argv[6]
# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
#print device.battery(batteryThreshold)

# Read BITalino version
device.version()

file = open(path,'w')
    
# Start Acquisition
device.start(samplingRate, acqChannels)

start = time.time()
end = time.time()
while (end - start) < running_time:
    # Read samples
    samp = device.read(nSamples)
    analog = []
    for j in range(0,nSamples):
    	analog.append([samp[j][b] for b in range(5,5+len(acqChannels))])
    	for b in range(5,5+len(acqChannels)):
    		message = "%d;%f\n"%(b-5,samp[j][b])
    		file.write(message)
    		print("{:d};{:f}".format(b-5,samp[j][b]))
    #print analog
    end = time.time()
    
# Stop acquisition
device.stop()
file.close()
# Close connection
device.close()
sys.exit(1);