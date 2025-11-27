#include <iostream>
#include <vector>
using namespace std;

int main() {
int number;
vector<int> v;
for ( int i=0;i<5;i++) {
	cout<<"enter a  number:";
	cin>>number;
	v.push_back(number);
	}

for (int i = 0; i < v.size(); i++) {
    cout << "element in vector  at" << i << "is" << v[i] << " "<<endl;
}
return 0;
}

