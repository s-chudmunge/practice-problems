#include <iostream>
#include <memory>
using namespace std;

int main() {
auto p = make_unique<int>(42);
cout<<*p<<endl;

auto q=move(p);
cout<<*q<<endl;
return 0;
}

