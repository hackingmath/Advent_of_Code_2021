"""https://adventofcode.com/2021/day/9
Lava flow elevation map"""

import time

start = time.time()

class Cell:
    def __init__(self,grid,n,r,c):
        self.grid = grid #grid list
        self.height = int(n)
        self.r = r
        self.c = c
        self.nbs = list()
        self.visited = False

    def generate_nbs2(self):
        if self.r > 0:
            self.nbs.append([self.r-1,self.c])
        if self.r <len(self.grid)-1:
            self.nbs.append([self.r+1,self.c])
        if self.c > 0:
            self.nbs.append([self.r,self.c-1])
        if self.c < len(self.grid[0]) - 1:
            self.nbs.append([self.r,self.c+1])

    def generate_nbs(self):
        if self.r > 0:
            self.nbs.append(int(self.grid[self.r-1][self.c]))
        if self.r <len(self.grid)-1:
            self.nbs.append(int(self.grid[self.r+1][self.c]))
        if self.c > 0:
            self.nbs.append(int(self.grid[self.r][self.c - 1]))
        if self.c < len(self.grid[0]) - 1:
            self.nbs.append(int(self.grid[self.r][self.c + 1]))

    def check_lowest(self):
        self.generate_nbs2()
        for n in self.nbs:
            if int(n) <= self.height:
                return False
        return True

    def generate_basin(self,celllist):
        basin_count = 1
        self.visited = True
        self.generate_nbs2()
        for n in self.nbs:
            c = celllist[100 * n[0] + n[1]]
            if not c.visited and not (c.height == 9):
                basin_count += (celllist[100*n[0]+n[1]].generate_basin(celllist))
        return basin_count

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day09.txt"
d=[x for x in open(loc,"rt").read().split()]
# file is split into 100 rows of 100-character-long strings of digits

def test():
    nbs_list = ['2199943210','3987894921','9856789892','8767896789','9899965678']
    cell_list = list()
    for r,row in enumerate(nbs_list):
        for c,num in enumerate(row):
            cell_list.append(Cell(nbs_list,num,r,c))
    total = 0
    for c in cell_list:
        if c.check_lowest():
            total += c.height + 1
            print(c.r,c.c,c.height,c.nbs,total)
    print("total:",total)
#test()

nbs_list = ['2199943210','3987894921','9856789892','8767896789','9899965678']

def product(arr):
    output = 1
    for i in range(-3,0):
        output *= sorted(arr)[i]
    return output

def part2_test():
    cell_list = list()
    for r, row in enumerate(d):
        for c, num in enumerate(row):
            cell_list.append(Cell(d, num, r, c))
    basin_list = list()
    for c in cell_list:
        if not c.visited and not(c.height == 9):
            basin_list.append(c.generate_basin(cell_list))
    #total = sum([basin_list])

    #print(sum(sorted(basin_list)[:3]))
    print(len(basin_list),basin_list)
    print(product(basin_list))

print(part2_test())

print("Time (sec):",round(time.time()-start,1))