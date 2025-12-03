#include <iostream>
using namespace std;

int safe_div(int a,int b) {
if (b==0) {
	throw "division by zero";
}
return a/b;
}

int main() {

int a,b;
cin>>a>>b;
try {
cout<<safe_div(a,b);
}
catch(const char* msg) {
cout<<"cannot divide by zero";
}
return 0;
}

