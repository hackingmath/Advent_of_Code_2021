"""Day 1 of 2021's Advent of code
December 1, 2021
https://adventofcode.com/2021/day/1"""

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day01.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        lst.append(int(line))

#print(lst[:10])

def increasing(mylist):
    output = 0
    for i,n in enumerate(mylist):
        if i > 0:
            if n > mylist[i-1]:
                output += 1
    #print("question1:",output)
    return output

"""Now group the measurements by threes
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
"""

triplist = list()
idx = 0
while idx < len(lst) - 2:
    triplist.append(lst[idx]+lst[idx+1]+lst[idx+2])
    idx += 1

#print("lst:",lst[:10])
#print("triplist:",triplist[:10])

print(increasing(triplist))