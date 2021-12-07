import time
import numpy as np

start = time.perf_counter()
def get_input():
   with open('inputs/day7.txt') as f:
      temp = f.readlines()
   
   init = temp[0].split(",")
   init[-1] = init[-1].strip("\n")
   for i, val in enumerate(init):
      init[i] = int(val)
   return init

def day7part1(init):
   med = np.median(init)
   fuel = 0
   for val in init:
      fuel += abs(val - med)
   return fuel

def day7part2(init):
   averages = [np.floor(np.mean(init)), np.ceil(np.mean(init))]   # get floor and ceil around mean if not .00
   res = []
   fuel = 0
   # compute fuel for floor vs ceil average
   for avg in averages:
      for val in init:
         diff = int(abs(avg - val))
         fuel += diff/2*(diff + 1)
      res.append(fuel)
   return min(res)


init = get_input()
print(day7part1(init))
print(day7part2(init))
print((time.perf_counter() - start)*1000, "ms")



