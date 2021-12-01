import numpy

data = numpy.loadtxt("inputs/day1.txt")

# day1 func 1
def find_increase(lines):
	increase = 0
	for i in range(1,len(lines)):
		if lines[i] > lines[i-1]:
			increase += 1
	return increase

# day1 func 2
def measure_window(data):
	increase = 0
	temp = data[0] + data[1] + data[2]
	for i in range(1, len(data) - 2):
		temp_sum = data[i] + data[i+1] + data[i+2]
		if temp_sum > temp:
			increase += 1
		temp = temp_sum
	return increase

# main
print(find_increase(data))
print(measure_window(data))