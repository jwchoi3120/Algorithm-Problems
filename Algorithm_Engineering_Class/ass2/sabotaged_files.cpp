/*
Description
---------------
In looking through her previously-sorted files, Dakota has realized that they are out of order. Fortunately the sabatour made only a quick change to each set of files, either turning around a whole segment of them (so that they are in the reverse order of what is expected) or by swapping two entires. Can you find a single reverse or swap operation that will restore her files to sorted order?

Input Format
---------------
The file line contains a value N, indicating how many files there are in this set.

The next N values (on the next line) indicate the IDs of each file.

Constraints
---------------
2 ≤ N ≤ 105
0 ≤ file id ≤ 106

Output Format
---------------
If the array is already sorted OR Dakota can fix it with a single "swap" or "reverse" operation, write "yes" on the first line. Otherwise write "no" on the first line.

If a single operation needs to be performed, begin the second line with "swap" or "reverse" indicating either the two file positions to swap -or- the first and last positions that need to all be reversed. (if both are possible provide the "swap" option)

NOTE: You should assume the first position is 1 for the purposes of this question.

Example 0
---------------
Sample Input
2
4 2

Sample Output
yes
swap 1 2

Explanation
---------------
The two files are numbered 4 and 2. These are out of order, but can clearly be fixed by swapping the two values. As such we print "yes" since it's possible to fix, and indicate that the needed fix is swapping position 1 and positions 2 (remember, that indexing starts at 1).

Example 1
---------------
Sample Input
3
3 1 2

Sample Output
no

Example 2
---------------
Sample Input
6
1 5 4 3 2 6

Sample Output
yes
reverse 2 5
*/

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main() {
	int N;
	int id;
	cin >> N;
	vector<int> vec;
	vector<int> vec2;
	if (N == 0){
	  return 0;
	}
	for (auto i = 0; i < N; i++) {
		cin >> id;
		vec.push_back(id);
		vec2.push_back(id);
	}

	sort(vec2.begin(), vec2.end());

	for (auto i = 0; i < N; i++) {
		if (vec[i] != vec2[i]) {
			if (vec.size() > 2) {
				int j = i + 1;
				while (j < N) {
					if (vec[j] != vec2[j]) {
						swap(vec[i], vec[j]);
						if (vec == vec2) {
							cout << "yes" << endl;
							cout << "swap " << i + 1 << " " << j + 1; 
							return 0;
						}
						else {
							swap(vec[i], vec[j]);
							reverse(vec.begin() + i, vec.begin() + j + 1);
							if (vec == vec2) {
								cout << "yes" << endl;
								cout << "reverse " << i + 1 << " " << j + 1;
								return 0;
							}
							else {
								reverse(vec.begin() + i, vec.begin() + j + 1);
							}
						}
					}
					j++;
				}
			}
			else if (vec.size() == 2) {
				swap(vec[i], vec[i + 1]);
				cout << "yes" << endl;
				cout << "swap " << 1 << " " << 2;
				return 0;
			}
		}
	}
	cout << "no";
}