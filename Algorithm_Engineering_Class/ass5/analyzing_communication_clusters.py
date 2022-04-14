'''
Description
---------------
Over time, exploration teams will build more communications bases and set them up at each site. However, there's still a problem! Some sites simply cannot be connected at all, no matter how many bases are used.

You must analyze a connectivity network and identify how many distinct (unconnected) components a graph is divided into.

Input Format
---------------
The first line contains N, the number of sites being analyzed, and M, the number of connections that will exist when all nodes are in place.
The next M lines each have two values identifying a pair of connected sites.

Constraints
---------------
1 ≤ N ≤ 200
1 ≤ M ≤ 10,000
0 ≤ site IDs < N

Output Format
---------------
Print the number of indepent site clusters in the input graph.

Example 0
---------------
Sample Input
9 10
0 3
0 4
0 5
1 2
1 6
1 8
2 8
3 7
4 7
6 8

Sample Output
2
'''

# dfs source : https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

def answer(dict, l):
    for k, v in dict.items():
        d = dfs(dict, k)
        if d not in l:
            l.append(d)
dict = {}
K = input().split()
N = int(K[0])
M = int(K[1])

for i in range(M):
    site = input().split()
    f = int(site[0])
    t = int(site[1])

    try:
        dict[f].append(t)

    except:
        dict[f] = [t]

    try:
        dict[t].append(f)

    except:
        dict[t] = [f]

l = []
answer(dict, l)
print(len(l))

