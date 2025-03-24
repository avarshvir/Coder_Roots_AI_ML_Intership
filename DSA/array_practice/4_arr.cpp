//Next Greater Element (NGE) for every element in given Array.
#include <iostream>
using namespace std;

void printNextGreaterElement(int arr[], int n) {
    // Array to store the NGE for each element
    int nge[n];
    
    // Initialize all elements of nge[] as -1
    for (int i = 0; i < n; i++) {
        nge[i] = -1;
    }
    
    // For each element, find its NGE
    for (int i = 0; i < n; i++) {
        // Look for the first greater element to the right
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > arr[i]) {
                nge[i] = arr[j];
                break;
            }
        }
    }
    
    // Print the result
    cout << "Element \t NGE" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " \t\t " << nge[i] << endl;
    }
}

int main() {
    int arr[] = {4, 5, 2, 25, 7, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printNextGreaterElement(arr, n);
    
    return 0;
}