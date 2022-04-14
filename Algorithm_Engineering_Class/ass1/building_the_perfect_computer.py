'''
Description
---------------
Dr. Xenovian has developed a fantastic new computer game, but it requires a new type of multi-core computer that she designed. The cores in this computer must come in multiples of 12 AND they must be arranged on the motherboard in a perfect square.

Atfter talking to each customer, Dr. Xenovian determines the minimum number of cores they need ( x ) and the maximum number of cores they can afford ( y ). Given this range in the number of cores possible, she then needs to calculate how many of these values are divisible by 12 (d ), how many are perfect squares ( s ), and how many values have both qualities ( b ).

Write a program to perform these calculations.

Input Format
---------------
The first line contains C, the number of customers she needs to perform calculations for. C ranges then follow, each on a new line.

Each test contains two space-separated integers denoting the MIN( x ) and the MAX( y ) number of cores, inclusive.

Constraints
---------------
1 ≤ C ≤ 100
1 ≤ x ≤ y ≤ 109

Output Format
---------------
With each customer result on a new line, print out d, s, and b (where d is the number of values divisible by 12, s is the number of perfect squares, and b is the number of values that meet both criteria).

Example 0
---------------
Sample Input
2
6 12
25 37

Sample Output
1 1 0
1 2 1

Explanation
---------------
Two customer orders are put in.

The first can afford a computer with 6 to 12 cores in it. Of those, only one possibility is a multiple of 12 (12 itself), one is a perfect square (9), and none meet both criteria.

The second customer can afford a computer with 25 to 37 cores. Of those, one is a multiple of 12 (36 cores), two are perfect squares (25 and 36) and one meet both criteria (36).

'''
import math
num = int(input())
while num:
    inp = input()
    inp = inp.strip().split()
    x = int(inp[0])
    y = int(inp[1])
    lists = []
    second_value = 0
    third_value = 0
    first_value = int((y / 12) - (int((x - 1) / 12)))
    sqrt_x = math.sqrt(x)
    sqrt_y = math.sqrt(y)
    floor_sqrt_x = math.floor(sqrt_x)
    while floor_sqrt_x <= math.floor(sqrt_y):
        lists.append(floor_sqrt_x ** 2)
        if x <= floor_sqrt_x ** 2 and floor_sqrt_x ** 2 <= y:
            second_value += 1
            if (floor_sqrt_x ** 2) % 12 == 0:
                third_value += 1
        floor_sqrt_x += 1
    print(first_value, second_value, third_value)
    num -= 1