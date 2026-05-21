#include <iostream>
#include <vector>

using namespace std;

int main(){
    int rows,cols;
    cin>>rows>>cols;
    vector<vector<int>> max(rows, vector<int>(cols, 0));
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            cin>>max[i][j];
        }
    }
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
        cout<<max[i][j]<<" ";
        }
        cout<<"\n";
    }
    
    return 0;
}