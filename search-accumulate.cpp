#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
int n;
cin>>n;

vector<int> v(n);

for ( int i=0;i<n;i++) {
	cin>>v[i];
}
int mx = *max_element(v.begin(), v.end());
int mn = *min_element(v.begin(), v.end());
int sum = accumulate(v.begin(), v.end(), 0);
cout<< mx <<" "<< mn <<" " << sum <<endl;
return 0;
}
