'''
Description
---------------
As each team of exploeres from Oganesson Dynamics arrives at their destination, the first thing they want to do is setup a communications base. But where should they put it?

To decide, they build a graph of the area. Each node represents a work site, and each edge indicates two sites that are close enough to communicate if one of them has the communications base. In fact, pairs of sites can relay through the base to communicate, as long as they are both connected to it. It can be slow, but it works well.

You must determine where to put the base such that the MOST pairs of sites can communicate.

Input Format
---------------
The first line contains N, the number of sites being analyzed, and M, the number of pairs (edges) that could potentially communicate.
The next M lines each have two values identifying all pairs of sites that could communicate with a base station at one of them.

Constraints
---------------
1 ≤ N ≤ 200
1 ≤ M ≤ 10,000
0 ≤ site IDs < N

Output Format
---------------
Output the count of how many PAIRS of sites would be able to communicate if the communications base were placed in the optimal position.

Example 0
---------------
Sample Input
5 7
0 1
0 2
0 3
1 2
1 3
1 4
2 3

Sample Output
10

Explanation
---------------
If a communications node is placed at size 1, it will connect to 0, 2, 3, and 4.

This means that there are 10 pairs that can communicate. Node 1 can directly communicate with each of the four others PLUS it can relay communications between (0,2), (0,3), (0,4), (2,3), (2,4), and (3,4).
'''

class Vertex:
    def __init__(self, node):
        self.site = node
        self.neighbors = []

    def __len__(self):
        return len(self.neighbors)

    def insert(self, neighbor):
        self.neighbors.append(neighbor)

class Graph:
    def __init__(self):
        self.dict = {}

    def __iter__(self):
        return iter(self.dict.values())

    def add(self, f, t):
        if f not in self.dict:
            self.dict[f] = Vertex(f)
        if t not in self.dict:
            self.dict[t] = Vertex(t)

        self.dict[f].insert(self.dict[t])
        self.dict[t].insert(self.dict[f])

graph = Graph()

K = input().split()
N = int(K[0])
M = int(K[1])
maximum = 0
answer = 0
for n in range(M):
    site = input().split()
    f = int(site[0])
    t = int(site[1])
    graph.add(f, t)

for vertex in graph:
    if maximum < len(vertex):
        maximum = len(vertex)

for i in range(maximum):
    answer += (i + 1)
print(answer)


