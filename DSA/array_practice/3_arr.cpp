//Write a program to insert the element at the  end of the given array: {10,20,30,40,50};

#include<iostream>
using namespace std;
int main(){
    int n = 5;
    int arr[n] = {10,20,30,40,50};

    int ele = 60;
    n++;
    arr[5] = ele; 

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }

}