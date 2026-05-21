#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<double> nums(n);
    
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    sort(nums.begin(), nums.end());
    cout<<nums[1]<<"\n"<<nums[nums.size() -2]<<endl;
    
    return 0;
}