import csv
import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np

filename = 'Accelerometer_Walking.csv'  #Just change this for eachh graph

time = []
x = []
y = []
z = []



def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

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



x_s = smooth(x,30)


plt.xlabel('Time (seconds)')
plt.ylabel('Rotation (r/s)')
plt.plot(time, x_s, label = "X")
# plt.plot(time, y, label = "Y")
# plt.plot(time, z, label = "Z")
plt.legend(bbox_to_anchor=(1.12, 1.15))
plt.title('MoveLeftAndRight Gyroscope')
plt.show()

