"""Day 5 of 2021's Advent of code
December 5, 2021
https://adventofcode.com/2021/day/5
Lines and Points"""

class Grid(object):
    def __init__(self,linelist):
        self.lines = list()
        for l in linelist:
            self.lines.append(((l[0].split(',')),(l[2].split(','))))
        self.points = [[0 for r in range(1000)] for c in range(1000)]

    def lines_to_points(self,pt):
        """Converts endpoints of line segments to points on segments"""
        x1,y1,x2,y2 = int(pt[0][0]),int(pt[0][1]),int(pt[1][0]),int(pt[1][1])
        if x1 == x2 or y1 == y2:
            #self.points[x1][y1] += 1
            #self.points[x2][y2] += 1
            if x1 == x2:
                if y2 > y1:
                    for y in range(y1,y2+1):
                        self.points[x1][y] += 1
                else:
                    for y in range(y2,y1+1):
                        self.points[x1][y] += 1
            else:
                if x2 > x1:
                    for x in range(x1,x2+1):
                        self.points[x][y1] += 1
                else:
                    for x in range(x2,x1+1):
                        self.points[x][y1] += 1
        else:
            slope = (y2-y1)/(x2-x1)
            if int(slope) in [1,-1]:
                if x2 > x1:
                    y = y1
                    self.points[x1][y1] += 1
                    for x in range(x1 + 1, x2 + 1):
                        y += slope
                        if y == int(y):
                            self.points[x][int(y)] += 1
                else:
                    y = y2
                    self.points[x2][y2] += 1
                    for x in range(x2+1,x1+1):
                        y += slope
                        if y == int(y):
                            self.points[x][int(y)] += 1

    def apply_lines(self):
        for pt in self.lines:
            self.lines_to_points(pt)

    def count_points(self):
        output = 0
        for row in self.points:
            for pt in row:
                if pt > 1:
                    output += 1
        return output

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day05.txt"

with open(loc)as f:
    lst = []
    for line in f.readlines():
        numstr = line.split()
        lst.append(numstr)

def test():
    print(lst[:5])
    testlines = [['0,9', '', '5,9'], ['8,0', '', '0,8'], ['9,4', '', '3,4'], ['2,2', '', '2,1'], ['7,0', '', '7,4'],
                 ['6,4', '', '2,0'], ['0,9', '', '2,9'], ['3,4', '', '1,4'], ['0,0', '', '8,8'], ['5,5', '', '8,2']]

    g = Grid(testlines)
    g.apply_lines()
    #print(g.points)
    print("points:",g.count_points())
    #print(g.lines[:5])
    """g.lines_to_points([('0','0'),('5','5')])
    g.lines_to_points([('2','0'),('4','6')])
    g.lines_to_points([('0','2'),('5','2')])"""
    print(g.points)
    """
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 2], 
    [0, 1, 2, 0, 1, 0, 1, 0, 0, 2], 
    [0, 1, 0, 1, 2, 1, 0, 0, 0, 1], 
    [0, 0, 1, 0, 3, 0, 0, 0, 0, 1], 
    [0, 0, 0, 2, 1, 1, 0, 0, 0, 1], 
    [0, 0, 1, 0, 3, 0, 1, 0, 0, 0], 
    [1, 2, 1, 2, 2, 0, 0, 1, 0, 0], 
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

"""

#test()

def main():
    g = Grid(lst)
    g.apply_lines()
    #print(g.points)
    print("points:",g.count_points())

main()