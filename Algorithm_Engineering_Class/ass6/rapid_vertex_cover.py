'''
Description
---------------
The scientists from Oganesson Dynamics have found an alien computer than can input a graph and rapidly determine whether it contains a clique of K vertices. The possibilites are endless, since they should now be able to solve any NP-Complete problem!

For example: they found a set of wormholes (that form a graph!) with space stations at each vertex. To activate a wormhole, they must first power at least one neighboring space station. Will K activated space stations be enough to get the entire network up and running?

That's the vertex cover problem!

Given that you have a K-Clique solver, you can convert instances of the vertex cover problem to K-Clique such that it always returns the same YES/NO answer?

The conversion is easy. If you convert your K to N - K (that is, looking for the opposite of the vertex cover), you will have converted to the independent set problem. Then if you toggle all edges (that is, remove all edges that were present and add in all of the edges that were originally missing) to produce the complement graph, you will have converted from the independent set problem to the clique problem. Once these conversions are done, you merely need to output the resulting problem instance.

Input Format
---------------
The first line contains three values, N, M, K.
N is the number of vertices in the graph (with IDs 0 through N - 1)
M is the number of edges in the graph
K is the number of vertices being tested for
The next M lines each describe an edge with two values indicating the IDs of the vertices being connected.

Constraints
---------------
1 ≤ N ≤ 200
1 ≤ M ≤ 10,000
0 ≤ K ≤ N

Output Format
---------------
You must output the converted problem instance for the K-Clique problem that would have the same YES/NO answer as the original vertex cover problem. Otherwise, it should have the same format as the input.

note: Each edge pair must have the lower ID first and be sorted in numerical order.

Example 0
---------------
Sample Input
5 6 3
0 1
0 2
0 4
1 4
2 3
2 4

Sample Output
5 4 2
0 3
1 2
1 3
3 4

Explanation
---------------
There are 5 vertices and 6 edges in the input graph; the question asks if 3 vertices can cover the graph.

To change this to independent set, we simply need to ask if the same graph has an independent set of size (5 - 3) = 2.

THEN to change this problem to K-Clique, we have to turn off the existing edges and turn on the ones that were missing in the original graph. There are (5 x 4 / 2) = 10 possible edges; 6 of them were in the original graph, but 4 were missing. We list only those four missing edges in out output.
'''

from operator import itemgetter
stuff = input().split()
N = int(stuff[0])
M = int(stuff[1])
K = int(stuff[2])
s = set()
for m in range(M):
  inp = input().split()
  f = int(inp[0])
  t = int(inp[1])
  right = (f, t)
  opposite = (t, f)
  s.add(right)
  s.add(opposite)

everything = set()
for i in range(N):
  for j in range(N):
    if i is not j:
      tup = (i, j)
      everything.add(tup)
answer = set()

part = everything - s
l = list(part)
l.sort(key=itemgetter(1))
l.sort(key=itemgetter(0))
print(N, len(part) // 2, N - K)

for tup in l:
  if tup not in answer:
      print(tup[0], tup[1])
  answer.add(tup)
  answer.add((tup[1], tup[0]))