#include <iostream>

using namespace std;

int main(){
    double x;
    double sum;
    double c;
    cin >> x;
    sum=0;
    c=0;
    while(x!=-1){
        sum = sum+x;
        cin >> x;
        c=c+1;
    }
    cout << sum/c;
}