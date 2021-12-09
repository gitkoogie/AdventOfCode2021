import time
import numpy as np

start = time.perf_counter()
def get_input():
   with open('inputs/day8.txt') as f:
      temp = f.readlines()
   
   inputs = []
   outputs = []
   for val in temp:
      strings = val.split(" ")
      inp = strings[0:10]
      outp = strings[11:]
      outp[-1] = outp[-1].strip("\n")

      inputs.append(inp)
      outputs.append(outp)
   return inputs, outputs

def day8part1(outputs):
   unique = 0
   for out in outputs:
      for val in out:
         if len(set(val)) == 2:     # 1
            unique += 1
         elif len(set(val)) == 3:   # 7
            unique += 1
         elif len(set(val)) == 4:   # 4
            unique += 1
         elif len(set(val)) == 7:   # 8
            unique += 1
   return unique


inputs, outputs = get_input()

print(day8part1(outputs))


