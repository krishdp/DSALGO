#include<iostream>
using namespace std;

vector<int> first;

vector<int> second(4, 20);

int numbers[] = {10, 20, 30, 40};
vector<int> third(numbers, numbers + 4);

vector<int> fourth(third);