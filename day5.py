import time
import numpy

start = time.perf_counter()
def get_input():
   with open('inputs/day5.txt') as f:
      temp = f.readlines()
   x1y1 = []
   x2y2 = []
   for i in range(len(temp)):
      t = temp[i].split(" ")
      x1y1.append(t[0])
      x2y2.append(t[2].strip("\n"))
   one = []
   two = []
   for i in range(len(x1y1)):
      one.append(x1y1[i].split(","))
      two.append(x2y2[i].split(","))

   # create matrix for res
   matrix = numpy.zeros((1000, 1000))

   return matrix, one, two

def day5part1():
   m, x1y1, x2y2 = get_input()
   marked = 0
   ex_marked = 0
   for i in range(len(x1y1)):
      # vert marking
      if x1y1[i][0] == x2y2[i][0]:
         start = int(min(int(x1y1[i][1]), int(x2y2[i][1])))
         end = int(max(int(x1y1[i][1]), int(x2y2[i][1])))
         ex_marked += end - start + 1
         for ind in range(start, end + 1):
            m[ind, int(x1y1[i][0])] += 1
            marked += 1
      # horizontal marking
      elif x1y1[i][1] == x2y2[i][1]:
         start = int(min(int(x1y1[i][0]), int(x2y2[i][0])))
         end = int(max(int(x1y1[i][0]), int(x2y2[i][0])))
         ex_marked += end - start + 1
         for ind in range(start, end + 1):
            m[int(x1y1[i][1]), ind] += 1
            marked += 1
   # compute result
   cnt = 0
   for i in range(len(m)):
      for j in range(len(m[0])):
         if m[i][j] > 1:
            cnt += 1
   return cnt

def day5part2():
   m, x1y1, x2y2 = get_input()
   marked = 0
   ex_marked = 0
   for i in range(len(x1y1)):
      # vert marking
      if x1y1[i][0] == x2y2[i][0]:
         start = int(min(int(x1y1[i][1]), int(x2y2[i][1])))
         end = int(max(int(x1y1[i][1]), int(x2y2[i][1])))
         ex_marked += end - start + 1
         for ind in range(start, end + 1):
            m[ind, int(x1y1[i][0])] += 1
            marked += 1
      # horizontal marking
      elif x1y1[i][1] == x2y2[i][1]:
         start = int(min(int(x1y1[i][0]), int(x2y2[i][0])))
         end = int(max(int(x1y1[i][0]), int(x2y2[i][0])))
         ex_marked += end - start + 1
         for ind in range(start, end + 1):
            m[int(x1y1[i][1]), ind] += 1
            marked += 1
      # else diagonal
      else: 
         coordOne = x1y1[i]
         coordTwo = x2y2[i]
         Xlist = []
         Ylist = []
         
         # create x list
         if int(coordOne[0]) < int(coordTwo[0]):
            Xlist = list(range(int(coordOne[0]), int(coordTwo[0]) + 1))
         elif int(coordOne[0]) > int(coordTwo[0]):
            Xlist = list(reversed(range(int(coordTwo[0]), int(coordOne[0]) + 1)))
        
         # create y list
         if int(coordOne[1]) < int(coordTwo[1]):
            Ylist = list(range(int(coordOne[1]), int(coordTwo[1]) + 1))
         elif int(coordOne[1]) > int(coordTwo[1]):
            Ylist = list(reversed(range(int(coordTwo[1]), int(coordOne[1]) + 1)))
         
         ex_marked += len(Xlist)
         for ind in range(len(Xlist)):
            m[Ylist[ind], Xlist[ind]] += 1
            marked += 1

   # compute result
   cnt = 0
   for i in range(len(m)):
      for j in range(len(m[0])):
         if m[i][j] > 1:
            cnt += 1
   return cnt


print(day5part1())
print(day5part2())


print((time.perf_counter() - start)*1000, "ms")