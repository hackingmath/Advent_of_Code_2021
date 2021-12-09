"""https://adventofcode.com/2021/day/6
Lanternfish reproducing"""

import numpy as np
import time

start = time.time()

class Fish(object):
    def __init__(self,age = 8,birthday =0):
        self.age = age
        self.birthday = birthday

    def reproduce(self,daylist):
        day = self.birthday
        for i in range(256):
            while self.birthday + self.age+1+7*i < 256:
                daylist[self.birthday + self.age+1+7*i]

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day06.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        numstr = line.split(",")
        #print(numstr[:10])
    lst = [int(n) for n in numstr]
    nums_arr = np.array(lst)

numdict = dict()
for n in lst:
    if n in numdict:
        numdict[n] += 1
    else:
        numdict[n] = 1

#print(numdict) #{3: 58, 5: 67, 2: 70, 4: 48, 1: 57}
#print(arr[:10])

def test(n,days):
    nums = np.array([n])
    for i in range(days):
        output = np.array([])
        for n in nums:
            if n == 0:
                output = np.append(output,6)
                output = np.append(output,8)
            else:
                output = np.append(output,n-1)
        nums = np.array(output)
        #print(output)
    return len(nums)

# for i in range(1,5):
#     print(i,test(i,80))

#print("1:",test(1,150)) #7
#print("2:",test(2,18)) #5
#print("3:",test(3,18)) #5
#print("4:",test(4,18)) #4
#print("5:",test(5,18)) #4

print("Time (sec):",round(time.time()-start,1))
start = time.time()

def main():
    """Recursive Method. Very slow on 256"""
    maxdays = 256
    testlist = [3,4,3,1,2]
    testdict = {3:2,4:1,1:1,2:1}
    #daynumlist = [[] for i in range(maxdays)]
    #daylist = [1 for i in range(maxdays)]
    def reproduce(births,birthday,age):
        newbirthday = birthday
        while newbirthday <= maxdays:
            if births == 0:
                newbirthday = newbirthday+age+1
                births = 1
            else:
                newbirthday += 7
            if newbirthday <= maxdays:
                #for i in range(maxdays-newbirthday+1):
                daylist[newbirthday-1:] += 1
                    #daynumlist[newbirthday].append(8)
                #print(daylist)
                reproduce(0,newbirthday,8)
        return daylist[-1]
    output = 0
    # for n in testdict:
    #     daylist = [1 for i in range(maxdays)]
    #     tn,rn = testdict[n],reproduce(0,0,n)
    #     print("n,tn,rn:",n,tn,rn)
    #     output += tn*rn
    n = 1
    daylist = np.ones(maxdays)#[1 for i in range(maxdays)]
    tn, rn = testdict[n], reproduce(0, 0, n)
    print("n,tn,rn:", n, tn, rn)
    return output

#print("Main:")
#print(main())

def offspring(agelist,maxdate):
    """Calculates how many offspring a fish
    born on a given birthday will have before
    the maxdate."""
    day = maxdate
    daydict = dict()
    total = len(agelist)
    birthdays = [9 + 6*i for i in range(50)]
    for d in range(maxdate,0,-1):
        for b in birthdays:
            if d - b <= maxdate:
                daydict[d+b] = 0
        elif 9 < maxdate-d:
            daydict[d] = 1 + daydict[d+7]
    ndict = dict()
    for n in agelist:
        ndict[n] = 1+ daydict[n+1]
        d = n+1
        while d<=maxdate-7:
            d += 7
            ndict[n] += 1 + daydict[d]
    return daydict,ndict

def birthday(maxdays,age=8):
    """Generates a list of days
    the fish will give birth"""
    bday = age + 1
    output = list()
    while True:
        output.append(bday)
        if bday+7 > maxdays:
            break
        bday += 7
    return output

testlist = [1,2,3,4]
print(offspring(testlist,18))

print("Time (sec):",round(time.time()-start,1))