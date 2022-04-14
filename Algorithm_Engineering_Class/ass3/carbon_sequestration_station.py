'''
Description
---------------
Oganesson Dynamics have blueprints for a carbon sequestration station that will pull carbon out of the atmosphere until it has been reduced to a target level.

Every day a station can pull a configurable number of units of carbon out of the atmosphere. Unfortunately, the amount removed must always be set to a power of two. So, it could pull 1, 2, 4, 8, 16, or 32 units in a day (or more!), but NOT exactly 5 or 20 units.

Given a starting number of units (N) and a goal number (G), can you figure out the fewest number of days it would take to reach the target?

Input Format
---------------
The first line will contain a value T indicating the number of planets (the number of test cases).
The next T lines will each contain two integers N, indicating a number of units of carbon in the atmosphere, and G, the goal number of units for when the station is finished.
Constraints

1 ≤ T ≤ 200,000
1 ≤ G ≤ N ≤ 264 - 1

Output Format
---------------
N lines, each indicating the number of days it would take to reduce the carbon of a given planet down to the target level.

Example 0
---------------
Sample Input
1
12 1

Sample Output
3

Explanation
---------------
There is a single planet with 12 units of carbon on it, which needs to be dropped to 1. Three days are needed for the station to reduce it:

Day one reduces the carbon by 8 units, since 8 (23) is the largest power of two less than 12. This leaves four units of carbon in the atmosphere.
Four is a power of two, but one unit of carbon must remain, so the second day reduces it by 2 (21).
The third and final day reduces it by 1 (20) to the target of 1.
'''

T = int(input())
while T:
    n = input().split()
    num = int(n[0])
    K = int(n[1])
    difference = num - K
    time = 0
    while difference >= 0:
        b = bin(difference)
        s = b[2:]
        big_power = int('1' + '0' * (len(s) - 1), 2)
        difference -= big_power
        time += 1
    print(time - 1)
    T -= 1