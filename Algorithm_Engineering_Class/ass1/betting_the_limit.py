'''
Description
---------------
Extinction is a complex card game involving betting. In the final phase of the game, each round players must bet the amount of money that the poorest player has remaining. When someone is out of money, they drop out of the game. Play continues until only one player remains.

Dr. Xenovian plays in an Extinction tournament. Assuming she starts the final phase of the game with the most money and wins every round, can you track how many of her opponents will remain each round?

Suppose Dr. Xenovian has six opponents with the following amounts of money left (in thousands of dollars):

5 4 4 2 2 8

Then, in the first round, should would bet $2,000, which will bankrupt two of the players. For the next round, four opponents are left with the following amounts of money:

3 2 2 _ _ 6

The above step is repeated until no opponents are left.

Input Format

The first line contains a single integer N indicating the number of opponents.

The next line contains N integers: a0 , a1 , ..., aN-1  separated by spaces, where a represents the amount of money that the i th player has.

Constraints
---------------
1 ≤ N ≤ 1000
1 ≤ ai ≤ 1000
Output Format

For each pass, print the number of opponents that remain.

Example 0
---------------
Sample Input
6
5 4 4 2 2 8

Sample Output
6
4
2
1

Explanation
---------------
In the first round, there are six opponents (provided in the input file).

Dr. Xenovian bets 2, driving out two of the opponents and leaving the four others with 3 2 2 and 6 respectively.

Dr. Xenovian bets 2 again, driving out two more opponents. The last two have 1 and 4 left.

Round three, the bet is 1, cutting down to one opponent with 3 left.

Finally the last opponent is eliminated and the game ends (no need to output 0).

'''

num = input()
num = int(num)
bet = input()
bet = bet.strip().split()
second_bet = bet.copy()
lowest = int(bet[0])
print(num)
while num > 0:
    for i in second_bet:
        if int(i) < lowest:
            lowest = int(i)
    for j in bet:
        if int(j) == lowest:
            ind = second_bet.index(j)
            second_bet.pop(ind)
            num -= 1
    if second_bet:
        lowest = int(second_bet[0])
    if num == 0:
        break
    print(num)