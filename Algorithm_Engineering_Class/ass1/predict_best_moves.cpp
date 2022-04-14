/*
Description
---------------
Dr. Abagale Xenovian, a reclusive mathematician and master of games, has found a potentially valuable exploit in her favorite video game. When she uses a special attack combination, one of two things happen:

1. If her score is even, she loses 99 points and then her score is multiplied by 3.

2. If her score is odd, she loses 15 points and then her score is multiplied by 2.

Note that all scores are limited to a max value of 1,000,000. Any score that hits that limit will immediately loop back around (so a score of 1,000,007 just becomes a score of 7). Likewise, any score that goes below zero ALSO loops around (so a score of -7 would become a score of 999,993).

Given a starting score ( S ) and a number of times the exploit is used ( k ), determine Dr. Xenovian's final score in the game.

Input Format
---------------
The first line is a number ( T ), indicating the number of test cases. The next T lines each have two values, S and k, indicating the starting score and the number of times the exploit is used, respectively.

Constraints
---------------
1 ≤ T ≤ 100
0 ≤ S ≤ 1,000,000
0 ≤ k ≤ 100

Output Format
---------------
T lines, each indicating the final score in the associated game.

Example 0
---------------
Sample Input
3
1000 1
1000 2
1000 5

Sample Output
2703
5376
94599
*/

#include <iostream>
using namespace std;
int main() {
  int T, S, k;
  cin >> T;
  while (T--){
    cin >> S >> k;
    while (k--){
      if (S % 2 == 1) {
        S -= 15;
        if (S <= 0) {
            S += 1000000; 
        }
        S *= 2;
        if (S >= 1000000){
          S %= 1000000;
        }
      }
      else{
        S -= 99;
        if (S <= 0) {
            S += 1000000; 
        }
        S *= 3;
        if (S >= 1000000){
          S %= 1000000;
        }
      }
    }
    cout << S << endl;
  }
}