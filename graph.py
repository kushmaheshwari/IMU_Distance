import csv
import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np

filename = '23_steps/Accelerometer.csv'  #Just change this for eachh graph

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

y_s = smooth(y,30)
y_s -= 9.8

# ind = -1
# for i in range(len(time)):
# 	if time[i] > 7:
# 		# print i
# 		ind = i
# 		break


# time_new = time[ind:]
# x_s_new = x_s[ind:]


step_count = 0
below = False

dots = [] 


for i in range(len(y_s)-1):
	if below == False and y_s[i-1] < y_s[i] and y_s[i+1] < y_s[i] and y_s[i] > .5:
		step_count += 1
		below = True
		dots.append((time[i],y_s[i]))
	if y_s[i] < 0:
		below = False





print step_count

plt.xlabel('Time (seconds)')
plt.ylabel('Rotation (r/s)')
plt.plot(time, y_s, label = "Y_S")

for i in range(len(dots)):
	plt.plot(dots[i][0],dots[i][1],'ro')

# plt.plot(time, x_s, label = "Y")
# plt.plot(time, z, label = "Z")
plt.legend(bbox_to_anchor=(1.12, 1.15))
plt.title('MoveLeftAndRight Gyroscope')
plt.show()

