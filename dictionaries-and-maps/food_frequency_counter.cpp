#include <iostream>
#include <map>

using namespace std;

int main(){
    map<string, int>foods;
    string food;
    cin>>food;
    while(food!="end"){
        foods[food]++;
        cin>>food;
    }
    for(auto& p : foods){
        cout << p.first << ": " << p.second << endl;
    }
    
    return 0;
}
