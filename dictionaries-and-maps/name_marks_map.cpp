#include <iostream>
#include <vector>
#include <array>
#include <map>

using namespace std;

int main(){
    int N;
    string name;
    int mark;
    cin>>N;
    int i=0;
    map<string, int>marks;
    while(i<N){
        cin>>name;
        cin>>mark;
        marks[name]=mark;
        i+=1;
    }
    for(auto& p : marks){
        cout << p.first << ": " << p.second << endl;
    }
    
    return 0;
}