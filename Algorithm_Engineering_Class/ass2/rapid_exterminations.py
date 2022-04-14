'''
Description
---------------
The ICKs (Indrassi Carnivorous Katydid) have gotten out of control and Millennium Jackson wants to wipe them all out. He realizes that the best way to do this is to get colonies wiped out as fast as possible. Given a series of jobs, how can he get each job done as quickly as possible?

You will be provided with a list of job requests, with the time each request arrives and how long the job will take to complete. Every time Millennium finishes a job, he should start on the SHORTEST one that he knows about. The completion time of a job is measured from the time the request comes in to the time Millennium has completed the job. You must output the AVERAGE completion time (rounded down to the nearest integer) that Millennium took to complete all jobs.

For example, assume three job requests come in at time 0, time 1, and time 2, and they will take Millennium 3, 9, and 6 hours respectively. Millennium will start on the first job at time zero, taking 3 hours to finish it. At time 3 he'll start on the third job (since it's the shortest one) and finish it at time 9 (3+6). Since this job came in at time 2, he would have taken 7 hours to complete it (9-2). Finally at time 9 he start on the second job, finishing it at time 18, for a total of 17 hours spent on it (18-1).

Given that the completion times for the three jobs were 3 hours, 7 hours, and 17 hours, he would have spend an average of (3+7+17)/3 = 9 hours per job, which is what you would output.

Input Format
---------------
The first line provides the value N, the total number of job request coming in.
The next N lines each have two values: the time the job arrives (Ti) and how long the job will take (Li)
Note that the job list may be unsorted.

Constraints
---------------
1 ≤ N ≤ 105
0 ≤ Ti ≤ 109
1 ≤ Li ≤ 109

Output Format
---------------
Display the integer part of the minimum average time that the job took.

Example 0
---------------
Sample Input
5
961148050 385599125
951133776 376367013
283280121 782916802
317664929 898415172
980913391 847912645

Sample Output
1418670047

Example 1
---------------
Sample Input
50
137857688 413115088
679783990 171274023
783725811 742261681
238387441 531682046
683427743 559301752
843391076 398722857
593760457 2628387
441381803 788912528
771854880 916901718
976015955 978145894
235492265 264125858
866638949 551120745
238176883 201620672
254029772 950305054
356294983 203393748
291672611 722032663
560013448 126478507
929678215 321924654
737812220 884493567
388266395 252551113
79292652 229453232
367753702 242882326
930211560 461283594
955372388 594944846
506995906 872449795
538015463 457419763
950540066 820099707
823860276 896193555
538832788 47584891
88242680 700680580
196842555 623621497
700528228 610051112
668066226 170226832
522278872 914689320
375621149 336628938
418416931 270027322
179882058 480538711
540671906 215602397
201411561 930064341
36616963 35887002
772894889 944088968
891134170 633761602
975099001 434725536
926070958 326905396
727328509 867529847
340789259 890185621
923620442 986091986
747688776 107231383
38070714 495529501
610348800 235616181

Sample Output
8485548331
'''

def insertion_sort(lists):

    for i in range(1, len(lists)):
        while 0 < i and lists[i][1] < lists[i - 1][1]:
            lists[i], lists[i - 1] = lists[i - 1], lists[i]
            i -= 1

    return lists

def main():
    N = int(input())
    big_list = []
    for i in range(N):
        small_list = []
        jobtimes = input().split()
        arrive = int(jobtimes[0])
        duration = int(jobtimes[1])
        small_list = [arrive, duration]
        big_list.append(small_list)
    big_list.sort()
    value = 0
    current = big_list[0][0]
    in_time_list = []
    in_time_list.append(big_list.pop(0))
    while in_time_list:
        start, dur = in_time_list.pop(0)
        current += dur
        value += (current - start)
        while big_list and big_list[0][0] <= current:
            j = 0
            if j < len(big_list):
                if current >= big_list[j][0]:
                    in_time_list.append(big_list.pop(0))
                else:
                    break
            else:
                break
            j += 1
        if big_list and not in_time_list:
            in_time_list = [big_list.pop(0)]
        insertion_sort(in_time_list)
    re_value = value // N
    print(re_value)
main()