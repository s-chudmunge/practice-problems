#include <iostream>
#include <algorithm>

using namespace std;

int main() {

string s;
cin>>s;
reverse(s.begin(),s.end());
cout<<s<<endl;
int pos = s.find("aa");
if (pos == string::npos)
	cout<< -1;
else 
	cout<<pos;
return 0;
}




