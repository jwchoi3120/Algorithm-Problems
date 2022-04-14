'''
Description
---------------
Some teams from Oganesson dynamics were sent with two communications bases. These bases must be connected to each other by an edge, but have the ability to relay messages through one another, connecting any of their neighbors and broadly expanding the range covered.

You must determine where to put the two bases such that the most pairs of sites can communicate.

Input Format
---------------
The first line contains N, the number of sites being analyzed and M, the number of pairs of sites that could potentially communicate, including through related messages.
The next M lines each have two values identifying all pairs of sites that could directly communicate if a base station is at one of them.

Constraints
---------------
1 ≤ N ≤ 200
1 ≤ M ≤ 10,000
0 ≤ site IDs < N

Output Format
---------------
Output the count of how many PAIRS of sites would be able to communicate if the communications bases were placed in the optimal position.

Example 0
---------------
Sample Input
5 6
0 1
0 2
0 4
1 4
2 3
2 4

Sample Output
10

Explanation
---------------
If communications nodes are placed at sites 0 and 2, they can facilitate communication among all 5 sites, this is allowed because sites 0 and 2 are connected to each other. On top of that, site 0 is connected to 1 and 4, while site 2 is connected to 3 and 4.

With fives sites, there are (5 x 4)/2 = 10 pairs.
'''

import math

def calculate(neighbor, range):
    fact = math.factorial
    return fact(neighbor) // fact(range) / fact(neighbor - range)

def answer(dict):
    maximum = 0
    for k, v in dict.items():
        s = set()
        for key, val in dict.items():
            if key in v:
                s = set(v).union(set(val))
            if len(s) >= maximum:
                maximum = len(s)

    return calculate(maximum, 2)

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

print(int(answer(dict)))

