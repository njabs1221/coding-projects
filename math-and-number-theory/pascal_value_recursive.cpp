
#include <iostream>
using namespace std;

int pascal(int row, int col){
    int prod=1;
    if(col==0) return prod;
    if(col==row) return prod;
    return pascal(row-1, col) + pascal(row-1, col-1);
    }


int main(){
    int r, c;
    cin >> r >> c;
    cout << pascal(r, c) << endl;
    return 0;
}