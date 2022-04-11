#include<iostream>
#include <array>
#include<algorithm>
using namespace std;



void update_arr(array<int, 6> &arr, int i, int val){
	arr[i] = val;

}


void print(const array<int, 6> arr){
	int n = arr.size();
	for (int i = 0; i< arr.size(); i++){
		cout<<arr[i]<<" ";
	}	
}

int main(){
	// int arr[] = {1,5,2,5,4};
	// int n = sizeof(arr)/sizeof(int);

	// for(int i = 0; i < n; i++){
	// 	cout << arr[i];
	// }
	array<int, 6> arr = {1,2,3,4,5,6};
	update_arr(arr, 0, 100);
	arr[0] = 12;
	sort(arr.begin(), arr.end());
	print(arr);
	return 0;
}
