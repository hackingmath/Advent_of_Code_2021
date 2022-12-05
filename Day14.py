"""https://adventofcode.com/2021/day/7
THEME"""

import time
from collections import defaultdict
from math import ceil

start = time.time()
loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day14.txt"
test_loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day14_test.txt"

def format_file(f):

    d=[x for x in open(f,"rt").read().strip().split('\n')]
    #polymer template
    pt = d[0]
    #pair insertion rules
    pin = [x.strip().split(' -> ') for x in d[2:]]
    #print(pin[-1]) # ['VS','B']
    pin_dict = {x[0]:x[1] for x in pin}
    #print(pin_dict['VV'])#S
    return pt,pin_dict

test_pt,test_pin_dict = format_file(test_loc)
pt,pin_dict = format_file(loc)

def part1(ptemp,pind,steps):
    letter_count = dict()
    for j in range(steps):
        output = ''
        for i,letter in enumerate(ptemp):
            if i == len(ptemp) - 1:
                output += letter
                break
            output += letter
            pair = ptemp[i:i+2]
            output += pind[pair]
        ptemp = output

        for letter in output:
            if letter in letter_count:
                letter_count[letter]+=1
            else:
                letter_count[letter] = 1
        #print(output)
        #find most and least frequent letters
        most,least,most_letter,least_letter = 0,1e06,'A','B'
        #print("Step",j)
        for letter in letter_count:

            if letter_count[letter]>most:
                most = letter_count[letter]
                most_letter = letter
            if letter_count[letter] < least:
                least = letter_count[letter]
                least_letter = letter
        #print(most - least)
    return most - least

def part2_1(ptemp,pind,steps):
    """Fills a dict with indices each step.
    in_dict: {0:'N',1:'N'... and so on. Next step the
    numbers are spread out and their in-between letter
    is inserted by the new index.
    Turns out this method is even slower than the first
    one!"""
    in_dict = {i:ptemp[i] for i in range(len(ptemp))}
    for j in range(steps):
        in_dict2 = {2*i:in_dict[i] for i in in_dict}
        #print(in_dict2)
        for k in range(len(in_dict)-1):
            in_dict2[2*k+1] = pind[in_dict2[2*k]+in_dict2[2*(k+1)]]
        in_dict = in_dict2.copy()
    counts = dict()
    for letter in in_dict.values():
        counts[letter] = sum(x==letter for x in in_dict.values())
    print("counts",counts)
    print(max(counts.values())-min(counts.values()))

def part2(letterstr,level,steps,pind,count_dict):
    """Recursively break AB into ACB and AC + CB
    Then you do that with the next pair"""

    if level == steps:
        #print("level = steps")

        if letterstr[1] in count_dict:
            #print(letter,"in counts")
            #print(count_dict)
            count_dict[letterstr[1]] += 1
        else:
            count_dict[letterstr[1]] = 1
        #return counts
    else:
        middle = pind[letterstr]
        #print("letterstring,middle:",letterstr,middle)
        part2(letterstr[0]+middle,level+1,steps,pind,count_dict)
        part2(middle+letterstr[1], level + 1, steps, pind,count_dict)
    #return counts


def f(in_str):
    counts = defaultdict()
    for i in range(len(in_str)-1):
        if in_str[i] not in counts:
            counts[in_str[i]] = 1
        else:
            counts[in_str[i]] += 1
        part2(in_str[i:i+2], 0, 40, test_pin_dict, counts)
    print(counts)
    print(max(counts.values()) - min(counts.values()))

def split_pair(pair,polymer_rules):
    middle = polymer_rules[pair]
    return pair[0]+middle,middle+pair[1]

def yet_another_part_2(letter_string,polymer_rules,steps):
    #dictionary for storing pairs
    string_dict = defaultdict()
    #put the first bunch of pairs in string_dict
    for i in range(len(letter_string)-1):
        #go pair by pair
        s = letter_string[i:i+2]
        string_dict[s] = string_dict.get(s,0)+1
        # if s in string_dict:
        #     string_dict[s] += 1
        # else:
        #     string_dict[s] = 1
    #print(string_dict)#check!
    for s in range(steps):
        #loop through string_dict, adding
        string_dict2 = defaultdict()
        for pair in string_dict:
            newpairs = split_pair(pair,polymer_rules)
            for np in newpairs:
                string_dict2[np] = string_dict2.get(np,0) + string_dict[pair]

        string_dict = string_dict2.copy()
    #after that loop, the string_dict will have the totals
    #for all the pairs. Count each letter
    letter_count_dict = defaultdict()
    for pair in string_dict:
        for letter in pair:
            letter_count_dict[letter] = letter_count_dict.get(letter,0) + string_dict[pair]
            # if letter in letter_count_dict:
            #     letter_count_dict[letter] += string_dict[pair]
            # else:
            #     letter_count_dict[letter] = string_dict[pair]
    #every letter will be counted twice
    for letter in letter_count_dict:
        letter_count_dict[letter] = ceil(letter_count_dict[letter]/2)
    print(string_dict)
    print(letter_count_dict)
    return max(letter_count_dict.values()) - min(letter_count_dict.values())
    #return string_dict


#print(part2('NNCB',test_pin_dict,20))
#print(part1(test_pt,test_pin_dict,10)) #1588 check!
#print(part1('NNCB',test_pin_dict,20))
#print(part1(pt,pin_dict,10)) #3259 in 1.3 sec
#print(part1(pt,pin_dict,40))
#print(split_pair('NN',test_pin_dict))
#print(yet_another_part_2("NNCB",test_pin_dict,40))#2188189693529 check!
print(yet_another_part_2(pt,pin_dict,40)) #3459174981021 in 0.0 seconds

print("Time (sec):",round(time.time()-start,1))