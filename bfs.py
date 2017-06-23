#!/usr/bin/python

# This uses breadth first search to find the shortest distance to each node in an undirected graph
# The input format:
'''
The first line indicates the number of queries
The second line is the number of nodes n and the number of edges m
The following m lines are the edges
Then the next line indicates the starting node
For example,
'2'
'4 2'
'1 2'
'1 3'
'1'
'3 1'
'2 3'
'2'
This should output
'1 1 -1'
'-1 1'
'''
# It construct the adjacency list first
# Then as it traverse the graph in breadth first manner, the distance to each node is recorded

# To run this on command line, enter
# chmod u+x bfs.py
# ./bfs.py
# give input as described as above


#import sys

num_query = int(input().strip())
for i in range(num_query):
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    adjacency = [[] for _ in range(n)]
    for i in range(m):
        u, v = input().strip().split(' ')
        u, v = [int(u), int(v)]
        adjacency[u - 1].append(v)
        adjacency[v - 1].append(u)
    s = int(input().strip())

    discovered = [0] * (n)
    discovered[s - 1] = 1

    L = [[s]]
    distance = [-1] * (n)
    distance[s - 1] = 0

    i = 0
    while (L[i]):
        L.append([])
        for u in L[i]:
            for v in adjacency[u - 1]:
                if discovered[v - 1] == 0:
                    discovered[v - 1] = 1
                    L[i + 1].append(v)
                    distance[v - 1] =  (i + 1)
        i += 1

    distance.remove(0)
    print(' '.join(map(str, distance)))