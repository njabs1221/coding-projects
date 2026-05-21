#include <iostream>

using namespace std;

int main() {
    string x;
    
    while (getline(cin, x)) {
        if (x == "end") {
            break;
        }
        
        int count = 0;
        for (char ch : x) {
            char lower = tolower(ch);
            if (lower == 'a' || lower == 'e' || lower == 'i' || 
                lower == 'o' || lower == 'u') {
                count++;
            }
        }
        
        cout << count << endl;
    }
    
    return 0;
}