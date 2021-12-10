"""https://adventofcode.com/2021/day/10
Character chunks"""

import time

start = time.time()

symbols = ['()','[]','{}','<>']
#scores = [57,1197,25137,3]
values = [1,2,3,4]

def identify_symbol(sym):
    """Takes in string symbol, tells which symbol
    it is, whether open (0) or close(1)"""
    for i, pair in enumerate(symbols):
        if sym in pair:
            return i, pair.index(sym)

#print(identify_symbol('{'))

def score_string(string):
    score = 0
    values = [0,1,2,3,4]# )]}> are 1,2,3,4
    for s in string:
        score *= 5
        n = identify_symbol(s)[0] + 1
        #character_list[n]+=1
        score += values[n]

    return score

#print(score_string('}}>}>))))'))

def test(string):
    """Goes through symbol list, if closing character,
    checks if previous is opening character and deletes
    both. Otherwise raises error."""
    place = 1
    while place < len(string):
        #print("place:",place)
        #print("in place:",string[place])
        #print("string:",string)
        i,c = identify_symbol(string[place])
        if c == 0:
            place += 1
        else:
            j,d = identify_symbol(string[place-1])
            if j == i:
                string=string[:place-1]+string[place+1:]
                place -= 1
            else:
                #print("Expected",symbols[j][1], "but found",symbols[i][1])
                return None
    return string[::-1],score_string(string[::-1])

#print(test('[({(<(())[]>[[{[]{<()<>>'))

inp = ['{([(<{}[<>[]}>{[]{[(<()>',
       '[[<[([]))<([[{}[[()]]]',
       '[{[{({}]{}}([{[{{{}}([]',
       '[<(<(<(<{}))><([]([]()',
       '<{([([[(<>()){}]>(<<{{']

def part1(inp):
    score = 0
    for string in inp:
        s = test(string)
        if s != None:
            score += scores[s]
    return score

#print(part1(inp))

class Chunk:
    def __init__(self,sym):
        self.open = True
        self.sym = sym
        self.char_list = [sym]
        self.turn = 0
        self.previous = None




    def apply_symbol(self,symbol):
        """takes in string symbol, switches turn to that number"""
        s,n = self.identify_symbol(symbol)
        if n == 0:
            self.previous = self.turn
            self.turn = s
        else: #close symbol
            #check if you can close that chunk
            if self.turn != s:
                return False

    def identify_turn(self):
        pass

def median(arr):
    sorted_arr = sorted(arr)
    print(sorted_arr)
    if len(arr)%2 == 1:
        return sorted_arr[len(arr)//2]
    return 0.5*(sorted_arr[len(arr)//2-1]+sorted_arr[len(arr)//2])

#print(median([2,5,4,1,3]))

def part2(arr):
    corrupted = 0
    stringlist = list()
    scorelist = list()
    for string in arr:
        if test(string) == None:
            corrupted += 1
        else:
            stringlist.append(test(string)[0])
            scorelist.append(test(string)[1])
    print(stringlist)
    print(scorelist)
    print(len(scorelist))
    print("corrupted:",corrupted)
    return median(scorelist)

inp2 = ['[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '(((({<>}<{<{<>}{[]{[]{}',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '<{([{{}}[<[[[<>{}]]]>[]]']

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day10.txt"
d=[x for x in open(loc,"rt").read().split()]
#print("d:",len(d))
tst = ['}}]])})]',')}>]})','}}>}>))))',']]}}]}]}>','])}>]']
#print(median([score_string(t) for t in tst]))
#first guess 2329833563 "too low"
#Since I was left with the beginning brackets,
# I was scoring the strings backwards.
#correct answer: 3515583998

print(part2(d))
#print(47//2)
print("Time (sec):",round(time.time()-start,1))