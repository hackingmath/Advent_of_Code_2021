"""Day 2 of 2021's Advent of code
December 2, 2021
https://adventofcode.com/2021/day/2"""

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day02.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        lst.append(line.split())

print(lst[:10])

def move(mylist):
    loc = [0,0]
    for n in mylist:
        if n[0] == 'forward':
            loc[0] += int(n[1])
        elif n[0] == 'down':
            loc[1] += int(n[1])
        else:
            loc[1] -= int(n[1])
    #print("question1:",output)
    return loc[0]*loc[1]

print(move(lst))

"""Now aim is added
"""
def move2(mylist):
    loc = [0,0]
    aim = 0
    for n in mylist:
        if n[0] == 'forward':
            loc[0] += int(n[1])
            loc[1] += aim*int(n[1])
        elif n[0] == 'down':
            #loc[1] += int(n[1])
            aim += int(n[1])
        else:
            #loc[1] -= int(n[1])
            aim -= int(n[1])
        print("loc:",loc,"aim:",aim)
    #print("question1:",output)
    return loc[0]*loc[1]

testlist = [['forward', '5'],['down','5'],['forward', '8'],['up', '3'],['down', '8'],['forward', '2']]

print(move2(lst))