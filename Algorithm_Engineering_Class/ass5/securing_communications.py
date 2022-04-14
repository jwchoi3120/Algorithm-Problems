'''
Description
---------------
Oganesson Dynamics wants to ensure that all of its communications within a network remain private, but this requires extra equipment for at least one end of each communicating pair of sites.

Given a graph where vertices represent work sites and edges represent pairs of sites that must be able to communicate securely, what are the fewest work sites that can have security-monitoring nodes to guarantee that each pair has at least one?

Hint: you will need to use a branch-and-bound approach to solving this problem.

note: For this problem, your program must be guaranteed to output the correct answer (or timeout in the process of searching). If your program's output is incorrect for a single test case, it will receive 0 credit on this problem (regardless of how many other test cases it passes). Timing out is allowed, however. Test cases on which you time out will result in no points from that test case, but will not zero out points earned on test cases where your program returned the correct output.

Input Format
---------------
The first line contains two values: the number of work sites (N) and the number of pairs of sites that must be able to communicate securely (M).
The next M lines each describe a pair of communicating sites, indicating the unique id of each.

Constraints
---------------
1 ≤ N ≤ 200
1 ≤ M ≤ 10,000
0 ≤ Work Site IDs < N

Output Format
---------------
A single number indicating the minimum number of work sites that must have security monitoring nodes to ensure that at least one exists for every communicating pair.

Example 0
---------------
Sample Input
5 6
0 1
0 2
0 4
1 4
2 3
2 4

Sample Output
3

Explanation
---------------
Security nodes at sites 0, 1, and 2 will ensure that all communications in the network are safe.

'''

from operator import itemgetter
class Pack(object):
    def __init__(self, total_skills, dict, N):
        self.vertex = total_skills
        self.dic = dict
        self.best_total = 201
        self.N = N
    def Solve(self, included, undecided):
        if len(undecided) == 0:
            return self.Eval(included)
        
        if len(included) >= self.best_total:
            return self.best_total
        
        if self.best_total == 1:
          return self.best_total
        p = undecided.pop()
        included.append(p)
        in_result = self.Solve(included[:], undecided[:])
        included.pop()
        for edge in dict[p]:
            if edge not in included:
                included.append(edge)
                if edge in undecided:
                    undecided.remove(edge)
        out_result = self.Solve(included[:], undecided[:])

    def Eval(self, included):
        if len(included) >= self.best_total:
            return self.best_total
        l = []
        for i in self.vertex:
            if i not in included:
                l.append(i)
        for ele in l:
            pairs = self.dic[ele]
            for i in pairs:
                if i not in included:
                    return False
        
        self.best_total = len(included)
        return self.best_total


dict = {}
K = input().split()
N = int(K[0])
M = int(K[1])
undecided = []
for i in range(M):
    site = input().split()
    f = int(site[0])
    t = int(site[1])

    try:
        dict[f].append(t)

    except:
        dict[f] = [t]

    try:
        dict[t].append(f)

    except:
        dict[t] = [f]
undecided = [(key, len(value)) for key, value in dict.items()]
undecided.sort(key = itemgetter(1))
l = [ item[0] for item in undecided ]
included = []
for key, value in dict.items():
  if len(value) == 1:
    if key in included:
      included.append(key)
    l.remove(key)
answer = Pack(l, dict, N)
answer.Solve(included, l[:])
print(answer.best_total)