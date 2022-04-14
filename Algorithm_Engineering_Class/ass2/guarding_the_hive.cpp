/*
Description
---------------
Queen Mellifluous has positioned her primary hive securely in a mountain pass, surrounded by N evenly-spaced outposts, all in a line. She has positioned K guards in a subset of those outposts, but is still concerned about an infiltrator sneaking in. Given a set of guard positions, can you identify the distance of the outpost furthest from the nearest guard?

Input Format
---------------
The first line has two values: N (the number of outposts, labeled 0 through N-1) and K (the number of guards on duty). The next K values indicate the outpost numbers where each guard is patrolling. For example, if there are 100 outposts and three guards at outposts 10, 60, 95, then an infiltrator coming in at the outpost 35 would be 25 outposts away from the nearest guard.

Constraints
---------------
1 ≤ k ≤ 109
1 ≤ N ≤ 105
0 ≤ guard positions ≤ k

Output Format
---------------
Output a single number indicating the farthest an infiltrator can be to the nearest guarded outpost as they try to sneak in.

Example 0
---------------
Sample Input
5 2
0 4

Sample Output
2

Explanation
---------------
Five outposts are available (0, 1, 2, 3, 4), with warriors at outposts 0 and 4. If an infiltrator attempts to sneak in by outpost 2, they will be two outposts away from any warrior, which is the best possible.


Example 1
---------------
Sample Input
6 6
0 1 2 4 3 5

Sample Output
0

Example 2
---------------
Sample Input
20 5
13 1 11 10 6

Sample Output
6

Example 3
---------------
Sample Input
90 17 
4 76 16 71 56 7 77 31 2 66 12 32 57 11 19 14 42

Sample Output
12

*/

#include <iostream>
#include <array>
#include <utility>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  int soldier;
  vector<int> places;
  vector<int> distances;
  cin >> N >> K;

  for(auto i = 0; i < K; i++) {
    cin >> soldier;
    places.push_back(soldier);
  }

  sort(places.begin(), places.end());
  for (auto i = 0; i < K; i ++){
  	if (K == N){
	      distances.push_back(0);
	      break;
	}
  	distances.push_back(places[i + 1] - ((places[i] + places[i + 1]) / 2.0));
  }
	sort(distances.begin(), distances.end());
	if (places[places.size() - 1] != N - 1) {
		if (distances.back() < 	N - 1 - places[places.size() - 1]){
			distances.push_back(N - 1 - places[places.size() - 1]);
		}
	}
	if (places[0] != 0) {
		if (distances.back() < places[0]){
			distances.push_back(places[0]);
		}
	}
  sort(distances.begin(), distances.end());
  if (K == N){
  	cout << 0 <<endl;
  }
  else{
	cout << distances.back() << endl;
  }
}