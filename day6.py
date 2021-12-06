import time
import numpy

start = time.perf_counter()
def get_input():
   with open('inputs/day6.txt') as f:
      temp = f.readlines()

   # get init states
   init_states = []
   init_states = temp[0].split(",")
   init_states[0] = init_states[0].strip("Initial state: ")
   init_states[-1] = init_states[-1].strip("\n")
   for i, val in enumerate(init_states):
   		init_states[i] = int(init_states[i])
   return init_states

def day6partX(init, days):
	age = numpy.zeros((9))
	curr_age = numpy.zeros((9))
	for val in init:
		age[val] += 1
		curr_age[val] += 1

	for i in range(days):
		for j in range(len(age)-1):		
			age[j] = curr_age[j + 1]
		age[8] = curr_age[0]
		age[6] = age[6] + curr_age[0]

		for k, val in enumerate(age):
			curr_age[k] = val

	return numpy.sum(age)

# friends code
def victor(init, days):
	bins = [0] * 9

	for fish in init:
		bins[fish] += 1

	for day in range(1, days + 1):
		index_0 = bins.pop(0)
		bins.append(index_0)
		bins[6] += index_0

	return numpy.sum(bins)


init = get_input()
print(day6partX(init, 80))
print((time.perf_counter() - start)*1000, "ms")

start = time.perf_counter()
print(day6partX(init, 256))
my_time = (time.perf_counter() - start)*1000
print(my_time, "ms")

start = time.perf_counter()
print(victor(init, 256))
victor_time = (time.perf_counter() - start)*1000
print(victor_time, "ms")

print("My code takes ", my_time/victor_time, "X longer than victors")


