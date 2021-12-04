"""Day 4 of 2021's Advent of code
December 4, 2021
https://adventofcode.com/2021/day/4
Playing Bingo"""

class Card(object):
    def __init__(self,cardlist):
        self.nums = cardlist
        #self.numbers_call = numlist
        self.won_cells = list()
        self.active = True

    def apply(self,n):
        """A number n is called. If it's in
        self.nums, put the location in the
        self.won_cells list."""
        for r,row in enumerate(self.nums):
            for c,numstr in enumerate(row):
                if int(n) == int(numstr):
                    self.won_cells.append([r,c])

    def check_win(self):
        if len(self.won_cells) < 5:
            return False
        for r in range(5):
            if [r,0] in self.won_cells and \
                    [r, 1] in self.won_cells and \
                    [r,2] in self.won_cells and \
                    [r, 3] in self.won_cells and \
                    [r, 4] in self.won_cells:
                #print('row',r)
                return True

        for c in range(5):
            if [0,c] in self.won_cells and \
                    [1,c] in self.won_cells and \
                    [2,c] in self.won_cells and \
                    [3,c] in self.won_cells and \
                    [4,c] in self.won_cells:
                #print("col",c)
                return True
        '''if [0, 0] in self.won_cells and \
                [1, 1] in self.won_cells and \
                [2, 2] in self.won_cells and \
                [3, 3] in self.won_cells and \
                [4, 4] in self.won_cells:
            print("diag_down")
            return True
        if [0, 4] in self.won_cells and \
                [1, 3] in self.won_cells and \
                [2, 2] in self.won_cells and \
                [3, 1] in self.won_cells and \
                [4, 0] in self.won_cells:
            print("diag_up")
            return True'''
        return False
    def sum_unmarked(self):
        total = 0
        for r in range(5):
            for c in range(5):
                if [r,c] not in self.won_cells:
                    total += int(self.nums[r][c])
        return total

    def print_card(self):
        for r in range(5):
            for c in range(5):
                if [r, c] not in self.won_cells:
                    print(self.nums[r][c])

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day04.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        numstr = line.split()
        lst.append(numstr)

"""The first element in the list is the list of chosen numbers.
Then there's a blank line and then the rows of each bingo card.
The 100 cards are separated by a blank line."""

def format_file(data):
    """Take in txt file and output list of numbers
    and a list of all the cards."""
    numlist = data[0][0].split(',')
    boardlist = list()
    r = 1
    for i in range(100):
        r+=1
        boardlist.append([])
        for j in range(5):
            boardlist[i].append(data[r])
            r+=1
    return numlist,boardlist

numlist,cardlist = format_file(lst)

print(numlist[:5])

def card_win(nlist,card):
    """Check how many numbers it takes
    for a given card to get bingo"""
    winlist = list() #cells with called numbers

def test_one_card():
    testcard = Card([['14','21','17','24','4'],
    ['10','16','15','9','19'],
    ['18','8','23','26','20'],
    ['22','11','13','6','5'],
     ['2','0','12','3','7']])

    testnums = ['7','4','9','5','11','17','23','2','0','14','21','24','10','16','13','6','15','25','12','22','18','20','8','19','3','26','1']
    for n in testnums:
        testcard.apply(n)
        print(n,testcard.check_win())
        if testcard.check_win():
            print('total:',testcard.sum_unmarked())
            break

def game():
    cards = [Card(clist) for clist in cardlist]

    for n in numlist:
        print('n:',n)
        #print("There are",len(cards),"cards left.")
        for c in cards:
            if c.active:
                c.apply(n)
                if c.check_win():
                    print("last number:",n)
                    print("total:",c.sum_unmarked(),int(n)*c.sum_unmarked())
                    if len(cards) == 1:
                        print(c.nums)
                        c.print_card()
                        return
                    c.active = False

game()