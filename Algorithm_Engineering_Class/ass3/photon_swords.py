'''
Description
---------------
The individual engineers at Oganesson Dynamics are most excited about the photon swords that they've discovered. Now they want to see just how hot they can make those swords without melting the handles.

Each sword has N buttons, each of which increases the heat by a fixed (integer) amount, to a limit of K (also an integer), beyond which the handle will melt. Given the amount of heat each button produces (B0 through BN-1), determine the maximum heat possible for the sword.

For example, if there were two buttons that put out 9 and 12 units of heat respectively, and the sword could handle a maximum of 31 units, you would be able to produce a maximum of 30 units by pressing the first button twice and the second button once. Any more presses and the device would melt. If there were also a button for 1 unit, you would be able to maximize the heat to a perfect 31.

Input Format
---------------
The first line contains T, the number of test cases.
Each test comprises two lines:
The first line contains two integers, N and K, representing the number of buttons and maximum heat, respectively.
The second line consists of space separated integers, B0 through BN-1, representing the heat output of each button.

Constraints
---------------
1 ≤ T ≤ 10
1 ≤ N, K ≤ 2000
1 ≤ Bi ≤ 2000

Output Format
---------------
Output T lines, the maximum heat that can be produced for each test case which is as near as possible including, but not exceeding, the heat limit ( K ).

Example 0
---------------
Sample Input
3
3 12
1 6 9
5 9
3 4 4 4 8
4 11
5 7 8 9

Sample Output
12
9
10

Explanation
---------------
In the first test case, you can press the '6' button twice to achieve the maximum heat output of 12.
In the second test case, you can press the '3' button three times to hit the maximum heat output of 9.
In the third test case, there is no way to reach the limit of 11, so the closest you can come is 10, by hitting the '5' button twice.

Example 5
---------------
Sample Input
1
8 10
11 12 13 14 15 16 17 3

Sample Output
9

Explanation
---------------
The first seven buttons are useless since they immediately overheat the sword. The best we can do is hit the last button three times for a heat total of 9.
'''

T = int(input())
while T:
    inp = input().strip().split()
    N = int(inp[0])
    K = int(inp[1])
    values = input().strip().split()
    B = []
    for i in range(N):
        B.append(int(values[i]))
    B.sort()
    every_num = []
    for i in range(N+1):
        every_num.append([0 for i in range(K+1)])

    for row in range(N+1):
        if row - 1 >= 0:
            check = B[row - 1]
        else:
            check = B[row]
        for column in range(K+1):
            remainder = column % check
            if remainder == 0:
                every_num[row][column] = max(every_num[row - 1][column], check * (column // check))
            elif column > check:
                every_num[row][column] = max(every_num[row][column - check] + check, every_num[row - 1][column])
            else:
                every_num[row][column] = every_num[row - 1][column]
    print(every_num[N][K])
    T -= 1