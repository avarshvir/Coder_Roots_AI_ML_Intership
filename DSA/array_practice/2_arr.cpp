//Write a program to insert the element at the  start of the given array: {10,20,30,40,50};

#include<iostream>
using namespace std;

int main(){
    int n = 5;
    int arr[n] = {10,20,30,40,50};
    
    int ele = 5;
    n++;

    for(int i = n; i > 0; --i){
        arr[i] = arr[i-1];
    }
    arr[0] = ele;

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }

}