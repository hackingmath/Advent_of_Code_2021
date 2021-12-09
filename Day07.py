"""https://adventofcode.com/2021/day/7
Crabs moving horizontally"""

import time

start = time.time()

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day07.txt"
d=[int(x) for x in open(loc,"rt").read().strip().split(',')]

testd = [16,1,2,0,4,2,7,1,2,14]
minx,maxx = min(d),max(d)

print(minx,maxx)#0, 1887
def min_fuel_req():
    min_fuel = 1e10
    for i in range(maxx):
        fuel_req = sum([0.5*abs(i-n)*(abs(i-n)+1) for n in d])
        #print(fuel_req)
        if fuel_req < min_fuel:
            min_fuel = fuel_req
            optimum = i
    return min_fuel,optimum

print(min_fuel_req())

print("Time (sec):",round(time.time()-start,1))