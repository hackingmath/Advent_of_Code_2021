"""https://adventofcode.com/2021/day/17
Trajectory of a projectile"""

import time

start = time.time()

"""
target area: x=96..125, y=-144..-98
"""


def trajectory():
    xmin, xmax, ymin, ymax = 96,125,-144,-98#20,30,-10,-5#
    dragx,dragy = 1,1
    highesty = [0,0,0]
    hits = list()
    for xvel1 in range(1000):
        for yvel1 in range(-1000,1000):
            xvel,yvel = xvel1,yvel1
            pos = [0, 0]
            #print("xvel,yvel:", xvel, yvel)
            hit_target = False
            high_y_in_run = 0
            while pos[1] > ymin and pos[0] < xmax:
                pos[0] += xvel
                pos[1] += yvel
                if pos[1] > high_y_in_run:
                    high_y_in_run = pos[1]
                    #print("high_y",high_y_in_run)
                if xmin<=pos[0]<=xmax and ymin<=pos[1]<=ymax:
                    hit_target = True
                    if [xvel1,yvel1] not in hits:
                        hits.append([xvel1,yvel1])
                    #print("hit target",pos,[xvel1,yvel1])
                #print(pos)
                xvel -= dragx
                if xvel < 0: xvel = 0
                yvel -= dragy


                #print("xvel,yvel,high_y_in_run:", xvel, yvel, high_y_in_run)
            if hit_target and high_y_in_run > highesty[0]:
                highesty = [high_y_in_run,xvel1,yvel1]

    return highesty,len(hits)
print(trajectory())

print("Time (sec):",round(time.time()-start,1))

"""
([10296, 14, 143], 546) too low, going too high in y-direction
Time (sec): 635.1

([10296, 14, 143], 796)
Time (sec): 9.5

([10296, 14, 143], 2371) Correct!
Time (sec): 9.4
"""