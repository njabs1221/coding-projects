#include <iostream>
using namespace std;

int fact(int n){
    int prod =1;
    if(n==0) return prod;
    for(int i=2;i<n+1;i++){
        prod*=i;
    }
    return prod;
}
int nChoose(int k, int b){
    return (fact(k)/(fact(b)*fact(k-b)));
}

int main(){
    int r;
    cin>>r;
    for(int i=0;i<r+1;i++){
        for(int j=0;j<i+1;j++){
            cout<<nChoose(i,j)<<" ";
        }cout<<endl;
    }
    return 0;


}