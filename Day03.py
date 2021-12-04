"""Day 3 of 2021's Advent of code
December 3, 2021
https://adventofcode.com/2021/day/3
The epsilon and gamma rates, by finding the most
common digit in each position in a list of binary numbers"""

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day03.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        numstr = line.split()
        lst.append(numstr[0])

print(lst[:10])

def binary_to_decimal(str):
    """Converts binary string to decimal"""
    n = len(str)-1
    num = 0
    for i in range(n,-1,-1):
        num += 2**i*int(str[n-i])
    return num

#print(binary_to_decimal('10010'))

def gamma(mylist):
    """Goes through each number in mylist and
    calculates the most common digit in each
    of the 12 positions"""
    binnum = ''
    digits = len(mylist[0])#number of digits
    for d in range(digits):
        sums = [0,0]
        for n in mylist:
            if n[d] == '0':
                sums[0] += 1
            else:
                sums[1] += 1
        if sums[0] > sums[1]:
            binnum += '0'
        else: binnum += '1'
    #create opposite for epsilon
    eps = ''
    for dig in binnum:
        if dig == '0':
            eps += '1'
        else:
            eps += '0'
    gamma_bin,eps_bin = binary_to_decimal(binnum),binary_to_decimal(eps)
    return gamma_bin*eps_bin

testlist = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
#print(gamma(testlist)) #198 check!

#print(gamma(lst))

"""Now calculate the oxygen generator and CO2 scrubber ratings"""

def frequent(mylist,place):
    """REturns the most common digit in the given place
    of the strings in mylist. If equal, returns '2'"""
    digits = len(mylist[0])#number of digits
    sums = [0,0]
    for n in mylist:
        if n[place] == '0':
            sums[0] += 1
        else:
            sums[1] += 1
    if sums[0] > sums[1]:
        return '0'
    elif sums[0] < sums[1]:
        return '1'
    else:
        return '2'

def oxygen(mylist,place):

    if frequent(mylist,place) == '0':
        newlist = [n for n in mylist if n[place] == '0']
    elif frequent(mylist,place) == '1':
        newlist = [n for n in mylist if n[place] == '1']
    else:
        newlist = [n for n in mylist if n[place] == '1']

    return newlist

def CO2(mylist,place):

    if frequent(mylist,place) == '0':
        newlist = [n for n in mylist if n[place] == '1']
    elif frequent(mylist,place) == '1':
        newlist = [n for n in mylist if n[place] == '0']
    else:
        newlist = [n for n in mylist if n[place] == '0']

    return newlist

def oxygen_rating(mylist):
    length = len(mylist[0])
    for i in range(length):
        newlist = oxygen(mylist,i)
        if len(newlist) == 1:
            return binary_to_decimal(newlist[0])
        mylist = newlist[::]

def CO2_rating(mylist):
    length = len(mylist[0])
    for i in range(length):
        newlist = CO2(mylist,i)
        if len(newlist) == 1:
            return binary_to_decimal(newlist[0])
        mylist = newlist[::]

print(oxygen_rating(lst)*CO2_rating(lst))