'''
Description
---------------
Oganesson is now building huge star ships capable of multi-year long missions. These ships need to have a large crew where there are many skills represented. Can you help them determine who should go?

But wait! Haven't you already solved this problem? Technically, you have, but now the crews are much larger and your old algorithm is too slow. In fact, any classical algorithm is going to be too slow to find a perfect answer. As such, you just need to find the best answer that you can -- and print out the full answer.

For this problem, you will be graded on how close your answer comes to the correct answer. For every test case, you MUST return AN answer (i.e., timing out will result in no points for the given test case); the quality of your answer will determine how much credit you receive on the test case.

Input Format
---------------
The first line has two values, N and K.
N represents the number of potential crew members available (numbered 0 through N - 1), and K is the number of distinct skills that need to be included (numbered 0 through K - 1).
The next N pairs of lines each provide information about a single person.
The first line for person i indicates the number of skills that person has (Pi), and the second line has Pi values indicating the specific skill IDs.
Constraints

N == 1000
500 ≤ K ≤ 1200
8 ≤ Pi ≤ 200

Output Format
---------------
You should output two lines. The first line indicates S, the size of the best solution you could find (the minimum number of people). The next line has S space-separated values indicating the specific IDs of the people to recruit onto the team.

Example 0
---------------
Sample Input
3 5
2
1 3
3
0 1 2
3
0 2 4

Sample Output
2
0 2

Explanation
---------------
There are three people to choose from in the example input, and five total skills. These people are then presented in order. Person 0 has 2 skills: 1 and 3. Person 1 has 3 skills: 0, 1, and 2. Person 2 also has 3 skills: 0, 2, and 4.

The output provided indicates that two people are choosen for the team, person 0 and person 2. Since these two people comprise the full set of skills, this answer would be deemed "correct" and would receive points. Given that it is also the minimal answer, it would receive the maximum number of points. If, instead, all three people were included in the answer, it would still be correct (since all of the skills would be covered), but it would not be minimal so it would receive fewer points.
'''

l = []
stuff = input().split()
N = int(stuff[0])
K = int(stuff[1])
for i in range(N):
    num = int(input())
    skills = input().split()
    skills = set(int(skill) for skill in skills)
    if skills not in l:
        l.append([i, skills])
l.sort(key=lambda x: len(x[1]), reverse=True)
l.sort(key=lambda x: x[0], reverse=True)
included = set()
everybody = []

while len(included) < K:
    skill_num, s = l.pop(0)
    everybody.append(skill_num)
    included |= s
    subtract = []
    for i in range(len(l)):
        l[i][1] -= included
        if len(l[i][1]) < 1:
            subtract.append(i)
    for j in range(len(subtract)):
        l.pop(subtract[j] - j)
    l.sort(key=lambda x: len(x[1]), reverse=True)

everybody.sort()

print(len(everybody))

while everybody:
    print(everybody.pop(0), end=" ")
