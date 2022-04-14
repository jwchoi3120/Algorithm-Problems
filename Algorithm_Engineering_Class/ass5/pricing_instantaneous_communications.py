'''
Description
---------------
Great news! Oganesson Dynamics has worked out the technology to provide instantaneous communications between two sites, MUCH faster than the old system. The problem is that it is quite expensive to setup, especially since a sending unit and receiving unit must be built for each site and the price varies depending on how far apart they are and if there are any obstacles in between.

Given a graph where nodes represent sites and edges provide the cost of connecting two sites, determine the cheapest it would be to make sure that ALL of the sites can communicate with one another. (Again, relaying of information is allowed, and much faster this time!)

Input Format
---------------
The first line contains N, the number of sites, and M, the number of possible pairs of sites that could communicate.
The next M lines each have three integer values. The first two identify the two sites involved, while the third provides the cost to setup a communications channel.
All graphs are gauranteed to be connected.

Constraints
---------------
1 ≤ N ≤ 200
1 ≤ M ≤ 10,000
0 ≤ cost to setup a communication channel ≤ 1,000,000
0 ≤ site IDs < N

Output Format
---------------
A single value indicating the minimum total cost to setup communications

Example 0
---------------
Sample Input
5 6
0 1 5
0 2 10
0 3 2
1 3 3
1 4 8
3 4 1

Sample Output
16
'''

def answer(dict, N):
    nodes = set()
    nodes.add(0)
    ans = 0

    while len(nodes) < N:
        edge = (0, 0, 1000000)
        for node in nodes:
            for t in dict[node]:
                if t[0] not in nodes and t[1] <= edge[2]:
                    edge = (node, t[0], t[1])
                elif edge[2] == 0:
                    break
        nodes.add(edge[1])
        ans += edge[2]

    return ans

dict = {}
K = input().split()
N = int(K[0])
M = int(K[1])

for i in range(M):
    site = input().split()
    f = int(site[0])
    t = int(site[1])
    cost = int(site[2])

    try:
        dict[f].append((t, cost))

    except:
        dict[f] = [(t, cost)]

    try:
        dict[t].append((f, cost))

    except:
        dict[t] = [(f, cost)]

print(answer(dict, N))
