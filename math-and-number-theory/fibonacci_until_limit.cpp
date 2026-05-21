#include <iostream>

using namespace std;

int main(){
    int x=1;
    int y=1;
    int z;
    int limit;
    cin>>limit;
    int a=0;
    string blank= " ";
    cout<<x;
    while(a<=0){   
        cout<<blank<<y;
        z=x+y;
        x=y;
        y=z;
        a=y-limit;
    }
    return 0;
}