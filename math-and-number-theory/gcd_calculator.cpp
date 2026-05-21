#include <iostream>
#include <cstdlib>

using namespace std;

int gcd(int a, int b) {
    a = abs(a);
    b = abs(b);

    while (b != 0) {
        int remainder = a % b;
        a = b;
        b = remainder;
    }

    return a;
}

int main() {
    int x, y;
    cin >> x >> y;
    cout << gcd(x, y) << endl;
    return 0;
}
