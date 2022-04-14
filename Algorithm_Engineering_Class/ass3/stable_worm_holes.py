'''
Description
---------------
Worm holes provide connections from one point in the galaxy to another. Unfortunately, they can have instabilities that will cause them to collapse when a ship tries to pass through them. Fortunately, Oganesson Dynamics Inc.'s top engineers have proposed a new way to build worm-hole stabilizers! Even better, these new stabilizers can repair multiple instabilities, if needed, though at an increasing cost for each additional one.

You have access to k stabilizers and there are n instabilities that need to be fixed. Each instability i has a base energy cost of ei terawatts. The first instability fixed by an individual stabilizer has its cost multiplied by × 1, the second by × 2, and so on, so that the kth instability costs × k.

Given n, k, and the base cost for each instability, find and print the minimum total energy (in terawatts) for all of the instabilities to be repaired.

Note: instabilities can be repaired in ANY ORDER.

Input Format
---------------
The first line contains two space-separated integers describing the respective values of n and k.
The second line contains n space-separated positive integers describing the respective values of e0, e1, ..., en-1

Constraints
---------------
1 ≤ n, k ≤ 100
1 ≤ ei ≤ 106
answer < 231
0 ≤ i < n

Output Format
---------------
 Print the total energy required to repair all of the instabilities.

Example 0
---------------
Sample Input
3 3
2 5 6

Sample Output
13

Explanation
---------------
There are three instabilities and three stabilizers. Since each stabilizer can fix one instability, there is only a mulitple of × 1 for each. The total cost is:

(2 × 1) + (5 × 1) + (6 × 1) = 13

Example 1
---------------
Sample Input
7 3
6 1 28 10 15 3 21

Sample Output
105

Explanation
---------------
There are seven instabilities and three stabilizers to fix them with.

The stabilizers can repair, in order:

first stabilizer: 28, 10, and 1
second stabilizer: 21 and 6
third stabilizer: 15 and 3
The first stabilizer would have an energy expenditure of 28 + 10×2 + 1×3 = 51

The second stabilizer would have an energy expenditure of 21 + 6×2 = 33

The third stabilizer would have an energy expenditure of 15 + 3×2 = 21

... for a grant total of 51 + 33 + 21 = 105.

'''

adding = 0
n = input().split()
N = int(n[0])
K = int(n[1])
inp = input().split()
l = []
for i in range(N):
    l.append(int(inp[i]))
l.sort(reverse = True)
big_list = []
for i in range(K):
    new_list = []
    big_list.append(new_list)
i = 0
for i in range(N):
    for j in range(K):
        if not l:
            break
        access = big_list[j]
        access.append(l.pop(0))
for i in range(K):
    for j in range(len(big_list[i])):
        adding += big_list[i][j] * (j + 1)
print(adding)