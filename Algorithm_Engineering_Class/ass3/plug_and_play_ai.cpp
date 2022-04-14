/*
Description
---------------
There are many types and sizes of smart bricks; all of them will automatically link together when touching. Given N types of bricks where each brick i has length Li , how many ways are there to lay them in a line with total length Ltotal ?

Input Format
---------------
The first line of the input provides T, the total number of test cases.
The next T pairs of lines describe a single test case:
The first line in a test case privides the number of brick types (N) and the total target length ( Ltotal ).
The second line has N values, each indicating the length of each available brick.

Constraints
---------------
1 ≤ T ≤ 10
1 ≤ N ≤ 50
1 ≤ Ltotal ≤ 106
1 ≤ Li ≤ 106

Output Format
---------------
T lines, one per test case, each indicating the number of combinations possible to make a line of that total length. Some of the values are quite large, so mod your answer by 1000000009.

Example 0
---------------
Sample Input
2
2 5
1 2
2 7
1 3

Sample Output
8
9
*/

#include <vector>
#include <iostream>
#include <stdint.h>
using namespace std;

uint64_t Question7(vector<uint64_t> nums, uint64_t K)
{
	uint64_t s = nums.size();
	vector<uint64_t> vec;
	for (auto i = 0; i <= K + 1; i++) {
		vec.push_back(0);
	}
	vec[0] = 1;
	for (auto i = 1; i <= K; i++) {
		int j = 0;
		while (j < s)
		{
			if (i >= nums[j])
			{
				vec[i] += vec[i - nums[j]];
				vec[i] = vec[i] % 1000000009;
			}
			j++;
		}
	}
	return vec[K];
}

int main()
{
	int T;
	cin >> T;
	while (T) {
		int N;
		uint64_t K;
		vector<uint64_t> nums;
		cin >> N >> K;
		for (auto i = 0; i < N; i++) {
			uint64_t L;
			cin >> L;
			nums.push_back(L);
		}
		cout << Question7(nums, K) << endl;
		T--;
	}
}