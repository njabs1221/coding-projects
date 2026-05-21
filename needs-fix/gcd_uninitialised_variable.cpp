#include <iostream>

using namespace std;

int main(){
    int x;
    int y;
    int gcd;
    cin>>x>>y;
    for(int i=1;i<=x;++i){
        if(x%i==0 && y%i==0){
            if(i>gcd){
                gcd=i;
            }
        }
    }
    cout<<gcd<<endl;
    return 0;
}
