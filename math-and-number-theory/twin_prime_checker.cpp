#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int N){
	if (N < 2) return false;
    for (int i = 2; i <= sqrt(N); i++){
        if (N % i == 0) return false;
    }
    return true;
}

bool isTwinPrime(int N){
	if (!isPrime(N)) return false;
    return isPrime(N - 2) || isPrime(N + 2);
}

int main(){
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i){
		int p;
		cin >> p;
		if (isTwinPrime(p)){
			cout << "true" << endl;
		}
		else{
			cout << "false" << endl;
		}
	}
	return 0;
}
