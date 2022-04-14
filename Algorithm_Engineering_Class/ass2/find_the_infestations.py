'''
Description
---------------
Millenium Jackson has a flood of infestation reports coming in, and he needs to decide which ones to deal with first. Can you examine the size of each report and let him know which infestations are the largest?

Input Format
---------------
The first line has two values N and K. N is the number of reports coming in, and K is the number that Millenium can deal with this month.

The next N lines indicate the size of each infestation.

Constraints
---------------
1 ≤ N ≤ 107
1 ≤ K ≤ 1000
1 ≤ infestation size ≤ 109

Output Format
---------------
 K values, indicating the K largest infestations in order (each on a new line).

Example 0
---------------
Sample Input
5 2
6
7
11
6
17

Sample Output
17
11

Explanation
---------------
There are five infestations, and we need to identify the largest two. They are size 17 and size 11.

Example 1
---------------

Sample Input
10 2
7
3
19
5
3
11
13
10
3
6

Sample Output
19 
13
'''

inp = input().strip().split()
n = int(inp[0])
k = int(inp[1])
num = []
while n:
    element = int(input())
    num.append(element)
    n -= 1
num.sort(reverse = True)
for i in range(k):
    print(num[i])