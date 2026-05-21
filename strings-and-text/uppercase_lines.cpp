#include <cctype>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        for (char &ch : line) {
            ch = toupper(static_cast<unsigned char>(ch));
        }

        cout << line << endl;
    }

    return 0;
}
