"""https://adventofcode.com/2021/day/18
Exploding Pairs"""

import time

start = time.time()

class Pair:
    def __init__(self,left,right,nestnum =0):
        self.left = left
        self.right = right
        self.nestnum = nestnum
        self.pair_list = [self.left,self.right]

    def __add__(self, other):
        return Pair(self.pair_list,other.pair_list,self.nestnum+1)

def main():
    a = Pair(1,1)

    b = Pair(2,2)
    c = a+b
    d = Pair(3,3)
    f = c+d

    print(f.pair_list,f.nestnum)

    # loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day18.txt"
    # d=[int(x) for x in open(loc,"rt").read().strip().split(',')]

#solution from PHOX
#https://colab.research.google.com/drive/1Ly9KJuE-inbN8RlvbdFO61jCLAqFaeky?usp=sharing#scrollTo=M1D9_54gKgTW
import functools, json, re
loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day18.txt"
with open(loc) as fp:
  data = list(map(json.loads, fp))

reg = lambda x: isinstance(x, int)
mag = lambda x: x if reg(x) else 3*mag(x[0])+2*mag(x[1])

def sub(s, n, ind):
  matches = list(re.finditer('\d+', s))
  if matches:
    start, end = matches[ind].span()
    s = s[:start] + str(int(s[start:end])+n) + s[end:]
  return s

def explode(num):
  num_s = json.dumps(num, separators=(',', ':'))
  for match in re.finditer('\[(\d+),(\d+)\]', num_s):
    pre, post = num_s[:match.start(0)], num_s[match.end(0):]
    if pre.count('[') - pre.count(']') >= 4:
      a, b = map(int, match.groups())
      num_s = sub(pre, a, -1) + '0' + sub(post, b, 0)
      break
  return json.loads(num_s)

def split(num):
  if reg(num):
    return [num//2, num - num//2] if num > 9 else num
  left_split = split(num[0])
  if left_split != num[0]:
    return [left_split, num[1]]
  return [num[0], split(num[1])]

def reduce(num):
  while True:
    new_num = explode(num)
    if new_num != num:
      num = new_num
      continue
    new_num = split(num)
    if new_num != num:
      num = new_num
      continue
    break
  return num

add = lambda a, b: reduce([a, b])

#part 1
#print(mag(functools.reduce(add, data))) #4391 correct!

#part 2
import itertools

print(max(mag(add(a, b)) for a, b in itertools.product(data, data)))

#Solution:
#4626
#Time (sec): 9.8
print("Time (sec):",round(time.time()-start,1))