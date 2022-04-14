'''
Description
---------------
Dr. Xenovian is playing a game where there are two possible moves each turn, one that earns a player x points and the other earns the player y points. The winner is the player closest to a given target score after n moves.

Given x, y, and n, can you calculate the set of all possible scores at the end of the game?

Input Format

The first line contains an integer T indicating the number of test cases.

The next T lines each describe a test case with three integers: x, y, and n.

Constraints
---------------
1 ≤ T ≤ 10
1 ≤ x, y, n ≤ 1000

Output Format
---------------
Space-separated list of numbers which are the possible total scores in increasing order.

Example 0
---------------
Sample Input
2
1 2 2
10 100 3

Sample Output
2 3 4
30 120 210 300

Explanation
---------------
Two test cases.

In the first, moves can score either 1 or 2 points and two moves are made. As such, there are three possible totals: 2 (if both moves score one), 3 (if one move scores one and the other move scores two, in either order), or 4 (if both moves score two).

In the second test case, moves score either 10 or 100 points and three moves are made. If they all score 10, the final score is 30. If one scores 100, it will be 120; if two score 100, it will be 210, and if all three score 100, it will be 300.

'''
num = int(input())

while num:
    ret = ''
    inp = input()
    inp = inp.strip().split()
    x = int(inp[0])
    y = int(inp[1])
    n = int(inp[2])
    result = []
    relist = []
    l = [x] * n
    Sum = sum(l)
    result.append(Sum)
    for i in range(n):
        l[i] = y
        plus = result[i] + (y - x)
        result.append(plus)
    s = set(result)
    result = list(s)
    result.sort()
    num -= 1
    ret = ' '.join(str(e) for e in result)
    print(ret)