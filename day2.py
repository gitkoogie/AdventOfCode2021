import numpy
import time

start = time.perf_counter()

with open('inputs/day2.txt') as f:
    lines = f.readlines()

# fix input   
temp = []
for i in range(len(lines)):
	t = lines[i].split(" ")
	temp.append(t[0])
	temp.append(t[1].strip("\n"))


#temp = ['forward', 5, 'down', 5, 'forward', 8, 'up', 3, 'down', 8, 'forward', 2]

def part1(temp):
	horizontal = 0
	depth = 0
	for i in range(0, len(temp), 2):
		if temp[i] == 'forward':
			horizontal += int(temp[i + 1])
		elif temp[i] == 'down':
			depth += int(temp[i + 1])
		elif temp[i] == 'up':
			depth -= int(temp[i + 1])
	return depth * horizontal

def part2(temp):
	aim = 0
	horizontal = 0
	depth = 0
	for i in range(0, len(temp), 2):
		if temp[i] == 'forward':
			horizontal += int(temp[i + 1])
			depth += aim * int(temp[i + 1])
		elif temp[i] == 'down':
			aim += int(temp[i + 1])
		elif temp[i] == 'up':
			aim -= int(temp[i + 1])
	return depth * horizontal



# part 1
print(part1(temp))
# part 2
print(part2(temp))
print((time.perf_counter() - start)*1000, "ms")