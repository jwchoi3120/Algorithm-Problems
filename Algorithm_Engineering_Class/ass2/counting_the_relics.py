'''
Description
---------------
ATOM labs has a regular inflow of priceless relics, some thought to have mystical powers. Dr. Malcolm Niacal is very interested in getting his hands on some of these relics and wants to keep track of how many are being studied in each lab location... just in case he wants to procure them for himself.

Input Format
---------------
The first line contains a single value N, indicating the number of relics being sent to labs to be studied.

The next N lines each contain the ID number of the research lab that each relic was sent to. Note that ID numbers may not be consecutive and can be large values.

Constraints
---------------
1 ≤ N ≤ 106
0 ≤ lab ID ≤ 1012
1 ≤ number of unique lab IDs ≤ 1000

Output Format
---------------
Print the ID number of the lab that has the most relics. If two labs have the same number of relics, just print the one with the lowest ID.

Example 0
---------------
Sample Input
8
63
63
63
8
3
8
63
3

Sample Output
63

Explanation
---------------
Eight relics are placed into three labs:

lab #3 has 2 relics
lab #8 has 2 relics
lab #63 has 3 relics
As such, lab #63 has the most relics, and thus, '63' is the output.

Example 1
---------------
Sample Input
15
97
97
29
68
68
97
97
83
97
68
29
97
68
83
83

Sample Output
97
'''

import operator
N = int(input())
numbers = dict()
while N:
    ele = int(input())
    if ele not in numbers:
        numbers[ele] = 1
    else:
        numbers[ele] += 1
    N -= 1
    
print(max(numbers.items(), key=operator.itemgetter(1))[0])