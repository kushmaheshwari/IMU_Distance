import csv
import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np
from numpy import trapz


filename = 'Training/30Steps/Accelerometer.csv'

time = []
x = []
y = []
z = []

with open(filename, 'r') as csvfile:

	csvreader = csv.reader(csvfile)
	for row in csvreader:
		i = 0

		for col in row:
			i_col = float(col)
			if i is 0:
				time.append(i_col)
			elif i is 1:
				x.append(i_col)
			elif i is 2:
				y.append(i_col)
			else:
				z.append(i_col)

			i+=1


start = time[0]
for i in range(len(time)):
	time[i] -= start
	time[i] *= .000000001

v = [None] * len(time)

v[0] = 0
for i in range(len(time) - 1):
	v[i+1] = y[i] * (time[i+1] - time[i]) + v[i]

print v


d = [None] * len(time)

d[0] = 0
for i in range(len(time) - 1):
	d[i+1] = v[i] * (time[i+1] - time[i]) + d[i]

print d


