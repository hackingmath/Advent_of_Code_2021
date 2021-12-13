"""https://adventofcode.com/2021/day/11
Octopi flashing
"""

import time

start = time.time()

def format_grid(arr):
    return [arr[10*i:(10*i+10)] for i in range(10)]

def string_to_list(string):
    output = [int(n) for n in string]
    return output

test_arr = '5483143223274585471152645561736141336146635738547841675246452176841721688288113448468485545283751526'
class Cell:
    def __init__(self,n,r,c):
        self.n = n
        self.r = r
        self.c = c
        self.nbs = list()
        self.flashed = False

    def list_nbs(self):
        self.nbs = list()
        if self.r > 0:
            self.nbs.append([self.r-1,self.c]) #up
            if self.c > 0:
                self.nbs.append([self.r-1,self.c-1]) #up-left
            if self.c < 9:
                self.nbs.append([self.r-1,self.c+1]) #up-right
        if self.c > 0:
            self.nbs.append([self.r, self.c - 1])  # left
        if self.c < 9:
            self.nbs.append([self.r, self.c + 1])  # right
        if self.r < 9:
            self.nbs.append([self.r+1,self.c]) #down
            if self.c > 0:
                self.nbs.append([self.r+1,self.c-1]) #down-left
            if self.c < 9:
                self.nbs.append([self.r+1,self.c+1]) #down-right
        return self.nbs

    def increment_nbs(self, clist):
        flashes = 0
        #print("incrementing")
        for cell in self.list_nbs():
            #print("cell:",cell)
            cx = clist[10*cell[0]+cell[1]]
            if not cx.flashed:
                #print("cx:",cx)
                if cx.n == 9:
                    cx.n = 0
                    cx.flashed = True
                    #print("incrementing",cx.r,cx.c)
                    cx.increment_nbs(clist)
                else:
                    #print("incrementing", cx.r, cx.c)
                    cx.n += 1
        return flashes

class Grid:
    def __init__(self,arr):
        self.arr = arr
        #print(self.arr)
        self.cellist = list()
        for r in range(10):
            for c in range(10):
                self.cellist.append(Cell(self.arr[r][c],r,c))
        self.flashes = 0

    def print_grid(self):
        output = ''
        for r in range(10):
            for c in range(10):
                output+=str(self.cellist[10*r+c].n)
            output += '\n'
        print(output)



    def step(self):

        for c1 in self.cellist:
            if c1.n == 9:
                c1.n = 0
                c1.flashed = True
                self.flashes += 1
                #print("flashing",c1.r,c1.c)
                self.flashes += c1.increment_nbs(self.cellist)
            else:
                if not c1.flashed:
                    #print("grid step inc",c1.r,c1.c)
                    c1.n += 1

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day11.txt"
d = ''
for x in open(loc,"rt").read().split():
    d += x
d_arr = format_grid(string_to_list(d))

def part1(arr,steps):
    t_arr = format_grid(string_to_list(arr))
    #print("t_arr:", t_arr)
    flashes = 0
    g = Grid(t_arr)
    for i in range(1,steps+1):
        for c in g.cellist:
            c.flashed = False
        #print(g.cellist[2].flashed)

        g.step()
        print("Step", i)
        g.print_grid()
        #check if all n's are the same
        if all(cell.n == g.cellist[0].n for cell in g.cellist):
            print("All the same!")
            break

        #print("1 4 neighbors:",g.cellist[14].nbs)
        flashes += sum([1 for c in g.cellist if c.flashed])
    print("flashes:",flashes) #1656 correct
part1(d,100)
#part1(test_arr,200) #195 correct
#part1(d,500)


print("Time (sec):",round(time.time()-start,1))