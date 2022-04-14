'''
Description
---------------
Portable shield generators can keep ships, buildings, and even people safe from harm. Oganesson Dynamics Inc. has a blueprint that will produce a device with a long series of aegis cells that can be individually turned on to produce a shield. Each cell has an individual contribution to shield strength. The total shield strength is the sum of these individual contributions.

There's a problem though! The cells get very warm when activated, and if you turn on two neighboring ones at the same time, they will overheat. What is the maximum total shield strength possible?

Given a series of N aegis cells where cell i, in order, has a shield strength of Si , determine the maximum total shield strength that can be generated.

HINT: an interactive webpage that will step you through a similar problem can be found at: http://www.cse.msu.edu/~ofria/cse431/DP/

Input Format
---------------
The first line provides N, the number of aegis cells in the row.
The second line has N values, separated by spaces, indicating the individual contributions to total shield strength (S0 through SN-1 ).

Constraints
---------------
1 ≤ N ≤ 106
1 ≤ Si ≤ 1010

Output Format
---------------
A single value indicating the maximum total shield strength possible.

Example 0
---------------
Sample Input
5
2 10 1 3 10

Sample Output
20

Explanation
---------------
There are five aegis cells, with shield levels of 2, 10, 1, 3, and 10, respectively.

If we activate the second and fifth cells, we will have a total of 20 shield strength (no other legal combination can produce more than 20).

Example 1
---------------
Sample Input
5
20 10 1 10 20

Sample Output
41

Explanation
---------------
There are five aegis cells, with shield levels 20, 10, 1, 10, and 20, respectively.

If we activate the first, middle, and last cells, we will have a total of 41 shield strength (no other legal combination can produce more than 41).
'''

def problem2(inp):
    first = 0
    second = 0
    third = 0
    for i in range(len(inp)):
        if i == 0:
            third = inp[0]
        elif i == 1:
            third = max(inp[0], inp[1])
        else:
            third = max(first, inp[i] + second)
        second = first
        first = third
    return third

def main():
    n = input().split()
    N = int(n[0])
    inpl = input().split()
    l = []
    for i in range(N):
      l.append(int(inpl[i]))
    print(problem2(l))
main()
