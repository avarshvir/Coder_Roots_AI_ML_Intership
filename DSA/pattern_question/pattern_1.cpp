/*
* * * * * 
* * * * 
* * *
* * 
*
*/


// method 1
/*
#include<iostream>
using namespace std;

int main(){
    for(int i = 5; i >= 0; i--){
        for(int j = i; j > 0; j--){
            cout << "*" << " ";
        }
        cout << endl;
    }
    return 0;
}
*/

// method 2

/*
#include<iostream>
using namespace std;
int main(){
    for(int i = 0; i < 5; i++){
        for(int j = i; j < 5; j++){
            cout << "*"<<" ";
        }
        cout << endl;
    }
}
*/