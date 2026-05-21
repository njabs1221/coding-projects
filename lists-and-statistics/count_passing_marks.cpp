#include <iostream>
#include <array>

using namespace std;

int main(){
    array<int, 10> myarray;
    int n;
    int c=0;
    for(int i=0;i<10;i++){
    cin>>myarray[i];
    }
    cin>>n;
    for(int j:myarray){
        if(j>=50){
            c=c+1;
        }
        
    }
    cout<<c;
    return 0;

}
