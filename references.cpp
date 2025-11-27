#include <iostream>
using namespace std;

int main() {
int a = 100;
int& r = a;
r=250;
cout<<a;
return 0;
}

