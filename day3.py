import time

start = time.perf_counter()
with open('inputs/day3.txt') as f:
   temp = f.readlines()

# fix input   
data = []
for i in range(len(temp)):
    data.append(temp[i].strip("\n"))

import numpy

#data = numpy.loadtxt("inputs/day3.txt")

#data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

gamma_rate = []
epsilon_rate = []

# func 1
def day1func1(data):
    for i in range(len(data[0])):
        sum_zero = 0
        sum_one = 0
        for j in range(len(data)):
            if int(data[j][i]) == 0:
                sum_zero += 1
            else:
                sum_one += 1
        if sum_zero > sum_one:
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")
    t1 = "0b"
    t2 = "0b"
    for i in range(len(gamma_rate)):
        t1 += gamma_rate[i]
        t2 += epsilon_rate[i]

    return int(t1, 2) * int(t2, 2)

# helper find 1 or 0 most common
def find(data, pos, v):
    sum_zero = 0
    sum_one = 0
    for i in range(len(data)):
        if int(data[i][pos]) == 0:
            sum_zero += 1
        else:
            sum_one += 1
    if v == 0:
        if sum_one >= sum_zero:
            return 1
        else:
            return 0
    elif v == 1:
        if sum_one < sum_zero:
            return 1
        else:
            return 0
    

# helper oxy
def oxygen(data):
    ret = ""

    ret += str(find(data, 0, 0))
    new = []
    for i in range(len(data)):
        if data[i][0] == ret[0]:
            new.append(data[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 1, 0))    
    new2 = []
    for i in range(len(new)):
        if new[i][1] == ret[1]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 2, 0))
    new = []
    for i in range(len(new2)):
        if new2[i][2] == ret[2]:
            new.append(new2[i])
    if(len(new) == 1):
        return new
    
    ret += str(find(new, 3, 0))    
    new2 = []
    for i in range(len(new)):
        if new[i][3] == ret[3]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2

    ret += str(find(new2, 4, 0))
    new = []
    for i in range(len(new2)):
        if new2[i][4] == ret[4]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 5, 0))
    new2 = []
    for i in range(len(new)):
        if new[i][5] == ret[5]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 6, 0))
    new = []
    for i in range(len(new2)):
        if new2[i][6] == ret[6]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 7, 0))
    new2 = []
    for i in range(len(new)):
        if new[i][7] == ret[7]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 8, 0))
    new = []
    for i in range(len(new2)):
        if new2[i][8] == ret[8]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 9, 0))
    new2 = []
    for i in range(len(new)):
        if new[i][9] == ret[9]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 10, 0))
    new = []
    for i in range(len(new2)):
        if new2[i][10] == ret[10]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 11, 0))
    new2 = []
    for i in range(len(new)):
        if new[i][11] == ret[11]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2

# func 2
def carbon(data):
    ret = ""

    ret += str(find(data, 0, 1))
    new = []
    for i in range(len(data)):
        if data[i][0] == ret[0]:
            new.append(data[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 1, 1))    
    new2 = []
    for i in range(len(new)):
        if new[i][1] == ret[1]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 2, 1))
    new = []
    for i in range(len(new2)):
        if new2[i][2] == ret[2]:
            new.append(new2[i])
    if(len(new) == 1):
        return new
    
    ret += str(find(new, 3, 1))    
    new2 = []
    for i in range(len(new)):
        if new[i][3] == ret[3]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2

    ret += str(find(new2, 4, 1))
    new = []
    for i in range(len(new2)):
        if new2[i][4] == ret[4]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 5, 1))
    new2 = []
    for i in range(len(new)):
        if new[i][5] == ret[5]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 6, 1))
    new = []
    for i in range(len(new2)):
        if new2[i][6] == ret[6]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 7, 1))
    new2 = []
    for i in range(len(new)):
        if new[i][7] == ret[7]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 8, 1))
    new = []
    for i in range(len(new2)):
        if new2[i][8] == ret[8]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 9, 1))
    new2 = []
    for i in range(len(new)):
        if new[i][9] == ret[9]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2
    
    ret += str(find(new2, 10, 1))
    new = []
    for i in range(len(new2)):
        if new2[i][10] == ret[10]:
            new.append(new2[i])
    if(len(new) == 1):
        return new

    ret += str(find(new, 11, 1))
    new2 = []
    for i in range(len(new)):
        if new[i][11] == ret[11]:
            new2.append(new[i])
    if(len(new2) == 1):
        return new2

def day1func2(data):
    oxy = oxygen(data)
    t = "0b"
    for i in range(len(oxy)):
        t += oxy[i]
    oxy = int(t, 2)

    co = carbon(data)
    t = "0b"
    for i in range(len(co)):
        t += co[i]
    co = int(t, 2)
    return co * oxy
    
print(day1func1(data))
print(day1func2(data))
print((time.perf_counter() - start)*1000, "ms")