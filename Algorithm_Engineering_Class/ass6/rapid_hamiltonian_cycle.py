'''
Description
---------------
The second super-fast computer found by Oganesson takes a graph and outputs a series of vertices that describes a Hamiltonian Cycle. Or at least it often does; sometimes it makes a mistake. You must write a program that takes the input graph and a set of output cycles, and then verifies if each one is correct.

Input Format
---------------
The first line contains N and M, the number of vertices and the number of edges in the input graph, respectively.
The next M lines each describe an edge, providing the IDs of the two vertices it connects.
The next line provides T, the number of test cycles.
The final T lines each provides a test cycle with N vertex IDs in the proposed order of traversal.

Constraints
---------------
5 ≤ N ≤ 1000
5 ≤ M ≤ 50,000
1 ≤ T ≤ 10
0 ≤ vi < N (for all vi, as vertex IDs)

Output Format
---------------
T lines, each with the word "YES" or "NO", indicating whether the associated test cycle is valid.

Example 0
---------------
Sample Input
5 6
0 2
0 3
1 3
1 4
2 4
3 4
3
1 3 0 2 4
0 1 2 3 4
2 0 3 1 4

Sample Output
YES
NO
YES 
'''

stuff = input().split()
N = int(stuff[0])
M = int(stuff[1])
dic = {}
for i in range(M):
    inp = input().split()
    f = int(inp[0])
    t = int(inp[1])

    try:
        dic[f].append(t)
    except:
        dic[f] = [t]
    try:
        dic[t].append(f)
    except:
        dic[t] = [f]

n = int(input())
l = []
for i in range(n):
    stuff = input().split()
    l.append(stuff)

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = int(l[i][j])
for small_list in l:
        flag = False
        for i in range(len(small_list)):
            set_list = set(small_list)
            length = len(small_list)
            if length > len(set_list) or small_list[(i + 1) % length] not in dic[small_list[i]]:
                print("NO")
                flag = True
                break
        if not flag:
            print("YES")