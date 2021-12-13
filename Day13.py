"""https://adventofcode.com/2021/day/13
Folding coordinate systems"""

import time

start = time.time()

#format test array
loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day13_test.txt"
d2=[x for x in open(loc,"rt").read().strip().split('\n')]

testlist = list()
for pt in d2:
    idx = pt.index(',')
    testlist.append([int(pt[:idx]),int(pt[idx+1:])])

#print(testlist[:10])
testtlist = [['y',7],['x',5]]

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day13.txt"
d=[x for x in open(loc,"rt").read().strip().split('\n')]
#print(d[-20:])
#print(d.index('')) #902
point_list1 = d[:902]
pointlist = list()
for pt in point_list1:
    idx = pt.index(',')
    pointlist.append([int(pt[:idx]),int(pt[idx+1:])])

#print(pointlist[:10])

#create list of transformations
tlist = list()
for t in d[903:]:
    idx = t.index('=')
    tlist.append([t[idx-1],int(t[idx+1:])])

#print(tlist)

def transform(pt,x,n):
    """Reflects pt by x or y (True/False)
    and a number n"""
    if x:
        newx = pt[0]-2*(pt[0]-n)
        return [newx,pt[1]]
    else:
        newy = pt[1] - 2 * (pt[1] - n)
        return [pt[0],newy]

def check_repeats(arr):
    output = list()
    for pt in arr:
        #print(pt)
        if pt not in output:
            output.append(pt)
    return output

def find_max_and_min(arr):
    minx,maxx,miny,maxy = arr[0][0],arr[0][0],arr[0][1],arr[0][1]
    for pt in arr:
        if pt[0] < minx:
            minx = pt[0]
        if pt[0] > maxx:
            maxx = pt[0]
        if pt[1] < miny:
            miny = pt[1]
        if pt[1] > maxy:
            maxy = pt[1]
    return minx,maxx,miny,maxy

def graph(arr,maxx,maxy):
    output = list()
    for y in range(maxy+1):
        output.append('')
        for x in range(maxx+1):
            if [x,y] in arr:
                output[y]+="#"
            else:
                output[y]+='.'
        #output.append('\n')
    for row in output:
        print(row)


def part1(arr,x,n):
    pointlist = list()
    if x:
        idx = 0
    else:
        idx = 1
    for pt in arr:
        if pt[idx] < n:
            pointlist.append(pt)
        else:
            newpt = transform(pt, x, n)
            if newpt not in pointlist:
                pointlist.append(newpt)
    return check_repeats(pointlist)

def part2(parr,tarr):
    for t in tarr:
        if t[0] == 'x':
            newarr = part1(parr,True,t[1])
        else:
            newarr = part1(parr, False, t[1])
        parr = newarr[::]
    return parr

# newtestlist = part1(testlist,False,7) #17 correct!
# ans = part1(newtestlist,True,5)
# print(ans)
# print(len(ans))
# print(check_repeats(ans))
# print(len(check_repeats(ans)))
#newlist = part1(pointlist,True,655)
#print(len(check_repeats(newlist)))

#p = part2(testlist,testtlist)

#print(len(p),p)

p = part2(pointlist,tlist)
print(len(p))
print(find_max_and_min(p))
graph(p,38,5)

print("Time (sec):",round(time.time()-start,1))