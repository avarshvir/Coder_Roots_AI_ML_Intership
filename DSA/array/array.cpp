#include <iostream>

using namespace std;

int main()
{
    int a = 10;
// array {}
            //  0,1,2,3,4,5
   int arr[] = {1,2,3,4,5,6};
   int sum = 0;
  // dataType variable[] = {value,value};
 
  //for loop  for(intialization; condition; increament/Decreament){
     
     
  //}
 
  cout<<sizeof(int)<<endl;
     
 
    int n = sizeof(arr) / sizeof(arr[0]);
   
    cout<<"Size of arr: "<<n<<endl;
     
     for(int i= 0; i< n; i++){
      // 3  =     2 +  1  
        sum  = arr[i] + sum;
        cout<<" Sum of array: "<<sum<<endl;
    }
     
    cout<<"Total Sum of array: "<<sum<<endl;
     

     
//   cout<<"Print the first Value: "<<arr[0]<<endl;
//     cout<<"Print the first Value: "<<arr[1]<<endl;
//      cout<<"Print the first Value: "<<arr[2]<<endl;
   
   

    return 0;
}

#include<iostream>

using namespace std;


bool isPrime(int num){
    if(num <=1){
        return false;
    }
   
    for(int i=2; i*i<= num; i++){
       
        if(num%i ==0){
            return false;
        }
       
       
    }
    return true;
}

int main(){
    int arr[] = {3, 4, 7, 10, 13, 17, 20, 21, 23};
   
    int n = sizeof(arr) / sizeof(arr[0]);
   
    for(int i=0; i<n; i++){
       if(isPrime(arr[i])){
           cout<<arr[i]<<" ";
       }
    }
}