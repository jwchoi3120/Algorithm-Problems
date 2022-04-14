/*
Description
---------------
Dakota Smith keeps finding new and interesting artifacts, each of which she sends off to ATOM labs for analysis. As ATOM finishes analyzing the artifacts, it sends them back to her.

Strangely, ATOM works on a Last-In-First-Out system, so Dakota either gets results back about an artifact immediately, or else she needs to wait a while to hear anything. As such, she always wants to know what the most valuable artifact she is waiting for is.

Input Format
---------------
The first line is an integer N, indicating the number of interactions Dakota will have with ATOM labs. The next N lines contain a number and possibly an item value (x) in the format:

1 x - Send an artifact of value x to the lab.
2   - Receive the most recent artifact back from the lab.
3   - Print the value of the most valuable item still at the lab.

Constraints
---------------
1 ≤ N ≤ 105
1 ≤ x ≤ 109

Output Format
---------------
 For each type 3 action, print the value of the most valuable artifact still in the lab, on a new line.

Example 0
---------------
Sample Input
10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3

Sample Output
26
91

Explanation
---------------
We take 10 different operations:

1) Push an artifact worth 97 onto the stack. Current: [97]
2) Remove the top of the stack; now empty.
3) Push an artifact worth 20 onto the stack. Current: [20]
4) Remove the top of the stack; now empty.
5) Push an artifact worth 26 onto the stack. Current: [26]
6) Push an artifact worth 20 onto the stack. Current: [26, 20]
7) Remove the top of the stack. Curent: [26]
8) Print the maximum element in the stack (which is 26)
9) Push an artifact worth 91 onto the stack. Current: [26, 91]
10) Print the maximum element in the stack (which is 91)

Example 1
---------------
Sample Input
4
1 83
3
2
1 76

Sample Output
83

*/

#include <iostream>
#include <vector>
using namespace std;
int main(){
  int N;
  vector<int> vec;
  cin >> N;
  while (N){
    int num;
    int value;
    cin >> num;
    if (num == 1){
      cin >> value;
      vec.push_back(value);
    }
    else if (num == 2){
      vec.pop_back();
    }
    else{
      int max = *vec.begin();
      for (auto it = vec.begin(); it != vec.end(); it++) 
        if (max < *it){
          max = *it;
        }
      cout << max << endl;
    }
    N--;
  }
}