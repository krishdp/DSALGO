#include<iostream>
#include<vector>
#include<string>
using namespace std;

//Complete this method, don't write main
vector<string> fizzbuzz(int n){
    vector<string> arr;
    for(int i = 1; i <= n; i++){
        if((n % 15) == 0){
            arr.push_back("FizzBuzz");
        } else if((n%3) == 0){
            arr.push_back("Fizz");
        } else if((n%5) == 0){
            arr.push_back("Buzz");
        } else{
            arr.push_back(to_string(i));
        }
    }
    return arr;
}

int main(){
    vector<string> res = fizzbuzz(10);
    for(string i : res){
        cout << i <<",";
    }
}