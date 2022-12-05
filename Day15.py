"""https://adventofcode.com/2021/day/15
Minimal path through grid"""

import time
from copy import deepcopy

start = time.time()

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day15.txt"
d=[x for x in open(loc,"rt").read().strip().split()]
nlist = list()
for r in d:
    nlist.append([int(s) for s in r])
#print(nlist)

test_loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day15_test.txt"
test_d=[x for x in open(test_loc,"rt").read().strip().split()]
#print(test_d)
test_list = list()
for r in test_d:
    test_list.append([int(s) for s in r])

def expand_row(row,addn):
    output = list()
    for n in row:
        if n + addn >= 10:
            output.append((n + addn)%9)
        else:
            output.append(n + addn)
    return output

def duplicate_grid(g):
    """Tiles grid 5 times to the right
    and 5 times down."""
    outg = list()
    for row in g:
        newrow = list()
        for i in range(5):
            newrow += expand_row(row,i)
        outg.append(newrow)
    newoutg = list()
    for i in range(5):
        for row in outg:
            newoutg.append(expand_row(row,i))
    return newoutg

#print(duplicate_grid(test_list))

def min_path(grid):
    '''grid is a nxn square array of digits'''
    n = len(grid)
    mgrid = min_grid(grid)
    path = list()
    #print("n:",n)
    r,c = 0,0
    while r<=n-1 and c <= n-1:


        #print(path)
        if r == n-1 and c == n-1:
            return sum(path),path
        elif c == n-1: #right edge
            r += 1
        elif r == n-1: #bottom row
            c+=1
        else:
            if mgrid[r][c+1] < mgrid[r+1][c]:
                c += 1
            else:
                r += 1
        path.append(grid[r][c])

def min_grid(grid):
    n = len(grid)
    # print("n:",n)
    mingrid = deepcopy(grid)
    #add values up first column on right
    for r in range(n-2,-1,-1):
        #add your value to cell above
        mingrid[r][n-1] += mingrid[r+1][n-1]
    for c in range(n-2,-1,-1):
        #add your value to the cell to the left
        mingrid[n-1][c] += mingrid[n-1][c+1]
    for r in range(n-2,-1,-1):
        for c in range(n-2,-1,-1):
            mingrid[r][c] += min(mingrid[r+1][c],mingrid[r][c + 1])
    #print("mgrid:",mingrid)
    return mingrid

def print_grid(g):
    for row in g:
        print(row)

tiny_d = [[1,1,6],[1,3,8],[2,1,3]]

#print(min_grid(tiny_d))
#print(min_path(test_list)) #40 check!
#big_test_list = duplicate_grid(test_list)
#print(min_path(big_test_list)) #315 check!
# big_tiny_d = duplicate_grid(tiny_d)
# print(big_tiny_d)

#big_nlist = duplicate_grid(nlist)
#print_grid(big_nlist)
#print(min_path(big_nlist)) #2908 wrong, too high
print("Time (sec):",round(time.time()-start,1))

"""
[[2, 4, 9, 4, 1, 8, 8, 7, 9, 5, 9, 4, 9, 3, 6, 8, 4, 2, 6, 6, 7, 2, 9, 3, 5, 9, 9, 7, 5, 5, 3, 4, 3, 6, 9, 9, 9, 1, 2, 3, 9, 7, 3, 8, 1, 7, 1, 1, 1, 4, 9, 4, 9, 7, 7, 9, 6, 6, 2, 9, 8, 8, 9, 6, 4, 7, 9, 2, 1, 3, 5, 6, 3, 8, 6, 8, 8, 2, 8, 7, 8, 7, 1, 1, 4, 7, 7, 4, 8, 7, 1, 9, 5, 9, 9, 9, 3, 4, 9, 5, 3, 5, 1, 5, 2, 9, 9, 8, 1, 6, 1, 5, 1, 4, 7, 9, 5, 3, 7, 7, 8, 3, 1, 4, 6, 1, 1, 8, 6, 6, 4, 5, 4, 7, 1, 1, 1, 2, 3, 4, 1, 8, 4, 9, 2, 8, 2, 2, 2, 5, 1, 5, 1, 8, 8, 1, 7, 7, 3, 1, 9, 9, 1, 7, 5, 8, 1, 3, 2, 4, 6, 7, 4, 9, 7, 9, 9, 3, 9, 8, 9, 8, 2, 2, 5, 8, 8, 5, 9, 8, 2, 1, 6, 1, 1, 1, 4, 5, 1, 6, 4, 6, 2, 6, 3, 1, 1, 9, 2, 7, 2, 6, 2, 5, 8, 1, 6, 4, 8, 8, 9, 4, 2, 5, 7, 2, 2, 9, 7, 7, 5, 6, 5, 8, 2, 2, 2, 3, 4, 5, 2, 9, 5, 1, 3, 9, 3, 3, 3, 6, 2, 6, 2, 9, 9, 2, 8, 8, 4, 2, 1, 1, 2, 8, 6, 9, 2, 4, 3, 5, 7, 8, 5, 1, 8, 1, 1, 4, 1, 9, 1, 9, 3, 3, 6, 9, 9, 6, 1, 9, 3, 2, 7, 2, 2, 2, 5, 6, 2, 7, 5, 7, 3, 7, 4, 2, 2, 1, 3, 8, 3, 7, 3, 6, 9, 2, 7, 5, 9, 9, 1, 5, 3, 6, 8, 3, 3, 1, 8, 8, 6, 7, 6, 9, 3, 3, 3, 4, 5, 6, 3, 1, 6, 2, 4, 1, 4, 4, 4, 7, 3, 7, 3, 1, 1, 3, 9, 9, 5, 3, 2, 2, 3, 9, 7, 1, 3, 5, 4, 6, 8, 9, 6, 2, 9, 2, 2, 5, 2, 1, 2, 1, 4, 4, 7, 1, 1, 7, 2, 1, 4, 3, 8, 3, 3, 3, 6, 7, 3, 8, 6, 8, 4, 8, 5, 3, 3, 2, 4, 9, 4, 8, 4, 7, 1, 3, 8, 6, 1, 1, 2, 6, 4, 7, 9, 4, 4, 2, 9, 9, 7, 8, 7, 1, 4, 4, 4, 5, 6, 7, 4, 2, 7, 3, 5, 2, 5, 5, 5, 8, 4, 8, 4, 2, 2, 4, 1, 1, 6, 4, 3, 3, 4, 1, 8, 2, 4, 6, 5, 7, 9, 1, 7, 3, 1, 3, 3, 6, 3, 2, 3, 2, 5, 5, 8, 2, 2, 8, 3, 2, 5, 4, 9, 4, 4, 4, 7, 8, 4, 9], 


"""