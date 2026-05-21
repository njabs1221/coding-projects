#include <iostream>

using namespace std;

int main(){
    double x;
    cin >> x;
    if(x>=75 && x<=100){
        cout << "First" << endl;
    }
    else if (x>=70){
        cout << "Upper second" << endl;
    }
    else if (x>=60){
        cout << "Lower second" << endl;
    }
    else if (x>=50){
        cout << "Third" << endl;
    }
    else{
        cout << "Fail" << endl;
    return 0;
    }


}