"""https://adventofcode.com/2021/day/7
THEME"""

import time

start = time.time()

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day07.txt"
d=[int(x) for x in open(loc,"rt").read().strip().split(',')]


print("Time (sec):",round(time.time()-start,1))