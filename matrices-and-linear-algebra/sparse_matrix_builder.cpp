#include <iostream>
#include <array>
#include <vector>
using namespace std;


int main(){
    int v,r;
    cin>>v>>r;
    
    int n;
    cin>>n;

    vector<vector<int>> arr(v, vector<int>(r));
    for(int i=0; i<n;i++){
        int v,r,value;
        cin>>v>>r>>value;
        arr[v][r]=value;
        
    }
    for (int i=0; i<v; i++) {
        for (int j=0; j<r; j++)
            cout << arr[i][j] << "\t";
        cout << "\n";
    }
    return 0;
}
