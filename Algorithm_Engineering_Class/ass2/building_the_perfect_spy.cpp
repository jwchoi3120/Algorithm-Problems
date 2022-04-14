/*
Description
---------------
Dr. Malcolm Niacal has simplified people down to their basic traits: height, weight, political leanings, conviviality, etc, each assigned a number. As he adds and removes numbers from his system, can you keep track of what the median value is? Warning, you might be working with a LOT of data!

The median of M numbers is defined as the middle number after sorting them in order if M is odd. Or it is the average of the middle two numbers if M is even. You start with an empty number list. Then, you can add numbers to the list, or remove existing numbers from it. After each add or remove operation, output the median.

Input Format
---------------
The first line is an integer, N, that indicates the number of operations. Each of the next N lines is either "a x" or "r x", with 'x' being an integer. An "a x" indicates that the value x is inserted (added) into the set, and "r x" indicates that the value x is removed from the set.

Constraints
---------------
1 ≤ N ≤ 106
-2,147,483,649 ≤ x ≤ 2,147,483,648

Output Format
---------------
For each operation:

If the operation is remove and the number x is not in the list, output "Wrong!" in a single line.
If the operation is remove and the number x is in the list, output the median after deleting x in a single line.
NOTE: If your median is 3.0, print only 3. And if your median is 3.50, print only 3.5. Whenever you need to print the median and the list is empty, print "Wrong!".

Example 0
---------------
Sample Input
7
r 1
a 1
a 2
a 1
r 1
r 2
r 1

Sample Output
Wrong!
1
1.5
1
1.5
1
Wrong!

Explanation
---------------
The list starts out empty, so the first input fails to remove anything and "Wrong!" is output.

The value 1 is then added, so the median is 1, which is printed.

The value 2 is then added, making the set [1, 2], and the median is 1.5.

Another 1 is added, making the set [1, 1, 2]. The median is now 1.

One of the 1's is removed, bringing the set back to [1, 2].

The 2 is removed, leaving only a single 1.

The final 1 is removed, meaning that there are no values left, resulting in a "Wrong!"

Example 1
---------------
Sample Input
50
a -2147483648
a -2147483648
a -2147483647
r -2147483648
a 2147483647
r -2147483648
a 10
a 10
a 10
r 10
r 10
r 10
r 100
r 100
r 100
r -2147483648
r 2147483647
r 10
a 1
a -1
a 1
a -1
r 1
r -1
r -1
r -1
r -1
r 1
r 1
r 0
a 0
a 1
a 2147483647
a 2
r 1
a 2147483646
r 2
a 2147483640
a 10
r 2
r 2
r 2
r 1
r 1
r 1
a 2147483640
a 2147483640
a -2147483648
a -2147483640
r 2147483640

Sample Output
-2147483648
-2147483648
-2147483648
-2147483647.5
-2147483647
0
10
10
10
10
10
0
Wrong!
Wrong!
Wrong!
Wrong!
-2147483647
Wrong!
-1073741823
-1
0
-1
-1
-1
-1073741823
Wrong!
Wrong!
-2147483647
Wrong!
Wrong!
-1073741823.5
0
0.5
1
1
2
1073741823
2147483640
1073741825
Wrong!
Wrong!
Wrong!
Wrong!
Wrong!
Wrong!
2147483640
2147483640
2147483640
1073741825
10
*/

#include <bits/stdc++.h> 
#include <vector>
#include <string>
using namespace std; 

double Median(vector<double> numbers)
{
  /* got an idea from stack over flow
  */
  int size = numbers.size();

    if (size % 2 == 0){
      return (numbers[size / 2 - 1] + numbers[size / 2]) / 2;
    }
    else{
      return numbers[size / 2];
    }
}
int Indexing(vector<double> list, double x){
  int place;
  for (int i = 0; i < list.size(); i++){
    if (list[i] == x) {
    place = i;
    return place;
    }
  }
  return -1;
}
string Fix(string median){
  string newone;
  for (int i = 0; i < median.length(); i++) {
    newone += median[i];
    if (median[i] == '.'){
      if (median[i + 1] != '0'){
        newone += median[i + 1];
        break;
      }
      else{
        newone.pop_back();
        break;
      }
    }
  }
  return newone;
}
int main() {
  int n;
  char command;
  double x;
  vector<double> list;
  cin >> n;
  while (n) {
    cin >> command >> x;
    if (command == 'a'){
      if (list.size() == 0) {
        list.push_back(x);
      }
      else if (x < list[0]){
        vector<double>::iterator i;
        i = list.begin();
        list.insert(i, x);
      }
      else if (x > list[list.size() - 1]) {
        list.push_back(x);
      }
      else {
        vector<double>::iterator i;
        i = lower_bound(list.begin(), list.end(), x);
        list.insert(i, x);
      }
      double median = Median(list);
      string str_median = to_string(median);
      string print_median = Fix(str_median);
      cout << print_median << endl;
    }
    else if (command == 'r'){
      int index = Indexing(list, x);
      if(index >= 0){
        list.erase(list.begin() + index);
        if (list.size()){
          double median = Median(list);
          string str_median = to_string(median);
          string print_median = Fix(str_median);
          cout << print_median << endl;
        }
        else{
          cout << "Wrong!" << endl;
        }
      }
      else{
        cout << "Wrong!" << endl;
      }
    }
    n--;
  }
}