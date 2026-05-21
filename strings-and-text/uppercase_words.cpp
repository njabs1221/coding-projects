#include <iostream>
#include <cctype>

using namespace std;

void toUpper(string& str){
	for (int i = 0; i < str.length(); i++){
        str[i] = toupper(str[i]);
	}
}

int main(){
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i){
		string line;
		cin >> line;
		toUpper(line);
		cout << line << endl;
	}
	return 0;
}
