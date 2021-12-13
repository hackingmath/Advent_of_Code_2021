"""https://adventofcode.com/2021/day/12
THEME"""

import time

start = time.time()

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day12.txt"
d=[x for x in open(loc,"rt").read().strip().split('\n')]
#print(d[:5])

loc = "C:\\Users\\Owner\\Documents\\AoC2021\\day12_test.txt"
d2=[x for x in open(loc,"rt").read().strip().split('\n')]
#print(d2)


test_graph1 = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']

def format_list_to_dict(arr):
    graph = dict()
    for con in arr:
        idx = con.index('-')
        a,b = con[:idx],con[idx+1:]
        #print(a,b)
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    return graph

def find_path(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    # if start not in graph:
    #     return None
    for node in graph[start]:
        if node.isupper() or (node.islower() and (node not in path)):
            newpath = find_path(graph,node,end,path)
            if newpath: return newpath
    return None

def find_all_pathsMINE(graph,start,end,path=[]):
    """Why on earth doesn't this work?
    replaced with one below"""
    path += [start]
    if start == end:
        print("start is end")
        return [path]
    if start not in graph:
        return []
    paths = list()
    for node in graph[start]:
        print(node)
        print(path)
        # if node.islower() and (node in path):
        #     continue
        if node not in path:
            newpaths = find_all_paths(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node.isupper() or (node not in path):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def count_lowers(arr):
    """Counts each lowercase thing in arr,
    if any are over 2, returns True."""
    twos = 0
    lowers = dict()
    for thing in arr:
        if thing not in ['start','end'] and thing.islower():
            if thing not in lowers:
                lowers[thing] = 1
            else:
                lowers[thing] += 1
                if lowers[thing] == 2:
                    twos += 1
                    if twos > 1:
                        return True
                if lowers[thing] > 2:
                    return True

    return False

def find_all_paths2(graph, start, end, path=[]):
    """Now one lowercase cave can be visited twice"""
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        #print(path)
        #print(node)
        #print(path.count(node))
        if node in ['start','end'] and node in path:
            continue
        if node.isupper() or not count_lowers(path):#(path.count(node)<2):
            newpaths = find_all_paths2(graph, node, end, path)
            for newpath in newpaths:
                if newpath not in paths:
                    paths.append(newpath)
    return paths

d_dict = format_list_to_dict(d)
print(d_dict)

test_graph1_dict = format_list_to_dict(test_graph1)
#print(test_graph1_dict)

d2_dict = format_list_to_dict(d2)
#print(d2_dict)

python_org_test_dict = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

larger_test = ['dc-end','HN-start','start-kj','dc-start','dc-HN','LN-dc','HN-end','kj-sa','kj-HN','kj-dc']
test2_dict = format_list_to_dict(larger_test)
#print(find_all_paths(python_org_test_dict,'A','D'))#works
#print(len(find_all_paths(d_dict,'start','end')))
#print(find_all_paths2(test_graph1_dict,'start','end'))
# t = find_all_paths2(test_graph1_dict,'start','end')
# for path in t:
#     print(path)
print(len(find_all_paths2(d_dict,'start','end')))
#print(len(find_all_paths2(test2_dict,'start','end')))

print("Time (sec):",round(time.time()-start,1))