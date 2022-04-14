/*
Description
---------------
Dr. Xenovian has many ideas for designing new board games. After she tries a set of new games, she also comes up with ways of merging those games to explore more possibilities. How many total new games can she make?

During each brainstorming session, Dr. Xenovian starts with n different ideas. She groups these into sets of m ideas to design each game. After that, for every c games she designs and plays, she can combine those games into yet one more game.

For example, assume she starts with n=4 ideas, plans to use only one new idea for each game (m = 1), and for every two games she plays, she will generate ideas for one new game idea (c = 2). Dr. Xenovian can design 4 games with her initial ideas, and then (after playing those games) comes up with 2 new games. When those new games finish, she can use them to generate yet another 1 game, for a grand total of 7 games ever.

Input Format
---------------
The first line contains a single integer T indicating the number of test cases.

The next T lines each have three integers, separated by spaces, indicating n, m, and c for that test case.

Constraints
---------------
1 ≤ T ≤ 1000
2 ≤ n ≤ 105
1 ≤ m ≤ n
2 ≤ c ≤ n

Output Format
---------------
For each test case, print the number of games that can be created during that brainstorming session.

Example 0
---------------
Sample Input
3
10 2 5
12 4 4
6 2 2

Sample Output
6
3
5

Explanation
---------------
Three brainstorming sessions:

Session one: 10 ideas to start with and each game needs 2 ideas, so five games can initially be designed. For every 5 games played, one new game can be designed, so only one additional game can be added this way, for a total of six.

Session two: 12 ideas to start with and each game needs 4 ideas. As such, three games are initially designed. Since four games need to be played to design a new one, we don't have enough and the initial three games are all there will ever be.

Session three: 6 ideas to start with, and each game needs 2 ideas, so three games can be initially designed. For every two games played, we can design a new one. This means that in round two, we can design one new game, with one played game left over. However, in round three, we can use the leftover game AND the new one to design yet another game. This process gives a grand total of 5 games.

*/

#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	while (T) {
		int n, m, c;
		cin >> n >> m >> c;
		int check = 0;
		int first;
		first = n / m;
		if (first < c) {
			cout << first << endl;
		}
		else if (first == c) {
			first += 1;
			cout << first << endl;
		}
		else {
			check += first;
			while (first >= c) {
				first++;
				first -= c;
				check++;
			}
			cout << check << endl;
		}
		T--;
	}
}