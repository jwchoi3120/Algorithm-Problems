#include <vector>
#include <iostream>
#include <stdint.h>
#include <ctime>
#include <unordered_set>
#include <fstream>
#include <set>
#include <algorithm>
using namespace std;

void BinarySearchTree(double n)
{
	int numbers = rand();
	multiset<int> s;
	for (auto i = 0; i < n; i++)
	{
		numbers = rand();
		s.insert(numbers);
	}
}
vector<int> LowerBound(vector<int> vec, int i, int n)
{
	std::vector<int>::iterator low = lower_bound(vec.begin(), vec.end(), n);
	vec.insert(low, n);
	return vec;
}


int main()
{
	ofstream file;
	file.open("time.txt");
	for (auto i = 10; i <= 100000000; i *= 10){
		double CLOCKS_PER_SEC;
		std::clock_t start_time = std::clock();
		BinarySearchTree(i);
		std::clock_t tot_time = std::clock() - start_time;
		std::cout << "Binary Search Tree Time: "
			<< ((double)tot_time) / ((double)CLOCKS_PER_SEC) << " seconds" << std::endl;
		
		int n = rand();
		vector<int> vec;
		int j = i;
		while (j) {
			int number = rand();
			vec.push_back(number);
			j -= 1;
		}
		sort(vec.begin(), vec.end());

		std::clock_t start_time_hash = std::clock();
		LowerBound(vec, i, n);
		std::clock_t tot_time_hash = std::clock() - start_time_hash;
		std::cout << "Lower Bound Time: "
			<< ((double)tot_time_hash) / ((double)CLOCKS_PER_SEC) << " seconds" << std::endl;

		
		
		file << i << " " <<((double)tot_time) / ((double)CLOCKS_PER_SEC) << " " << ((double)tot_time_hash) / ((double)CLOCKS_PER_SEC) << endl;

	}
	file.close();
}