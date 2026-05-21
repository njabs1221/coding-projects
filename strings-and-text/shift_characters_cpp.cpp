#include <iostream>

using namespace std;

int main(){
    string x;
    cin >> x;
    string result = "";  
    for (char ch : x) {
        char c = ch + 1;
        result += c;
    }
    
    cout << result << endl;
    
    return 0;
}