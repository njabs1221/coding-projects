#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    for (int i = 0; i <= n; i++) {
        string s;
        getline(cin, s);
        
        for (int j = 0; j < s.length(); j++) {
            s[j] = toupper(s[j]);
        }
        
        cout << s << "\n";
    }
    
    return 0;
}