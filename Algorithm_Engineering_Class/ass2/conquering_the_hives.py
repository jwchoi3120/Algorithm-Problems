'''
Description
---------------
Queen Mellifluous has found a neighboring planet with a series of hives around its equator. You must help her determine which hive to initiate the invasion from such that she will be able to sweep around the planet and have enough warriors to win each battle.

She knows how many warriors she will gain for winning each hive and how many warriors she will need to then expend to claim the next hive. She can conquor the first hive from orbit (without expending warriors)-- can you identify which hive she must begin the invasion with in order to have enough troops to defeat each of the others as she reaches them?

Input Format
---------------
The first line will contain the number of hives on the planet(N).
The next N lines will each contain a pair of integers, indicating the number of warriors that the queen will gain if she wins (or chooses as her starting point) that hive and how many warriors she needs to defeat next hive.

Constraints
---------------
1 ≤ N ≤ 105
1 ≤ warriors gained, warriors needed ≤ 109
We guarantee that there is a solution.

Output Format
---------------
 A single value indicating the lowest position of a hive where she can start her attacks.

Example 0
---------------
Sample Input
3
1 5
10 3
3 4

Sample Output
1

Explanation
---------------
There are three hives available here. The hive at position 0, provides only one warrior, but we need five just to get to the next hive so we can't start there.

We CAN, however, start at position 1. This hive would give 10 warriors, three of whom would be used to take hive 2. That leaves us with 7 warriors, plus we would get three more at hive 2, for a total of 10 again. Now we need to use four of those to get hive 0 (looping back around). We've now claimed all three hives!

As such hive 1 is the first one we can start at to claim all of the other hives as well.

Example 1
---------------
Sample Input
20
1 11
2 12
3 13
4 14
5 15
6 16
7 17
8 18
9 19
10 20
11 1
12 2
13 3
14 4
15 5
16 6
17 7
18 8
19 9
20 10

Sample Output
10

Example 3
---------------
Sample Input
20
5 15
16 6
2 12
3 13
14 4
7 17
1 11
13 3
20 10
15 5
6 16
4 14
9 19
11 1
8 18
17 7
18 8
12 2
10 20
19 9

Sample Output
---------------
7
'''

N = int(input())
big_list = []
for i in range(N):
    overall = input().strip().split()
    first = int(overall[0])
    second = int(overall[1])
    small_list = [first, second]
    big_list.append(small_list)
start = 0
check = N
i = 0
while check:
    if start + big_list[i % N][0] >= big_list[i % N][1]:
        start += big_list[i % N][0]
        start -= big_list[i % N][1]
        check -= 1
    if start + big_list[(i + 1) % N][0] - big_list[(i + 1) % N][1] < 0:
        start = 0
        check = N
    i += 1
re = i - N
print(re)
