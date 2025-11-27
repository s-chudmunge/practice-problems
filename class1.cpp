#include <iostream>
using namespace std;

class Rectangle {
public:
	int length;
	int width;
	int area(){return length*width;}
};
int main() {
Rectangle r;
r.length = 5;
r.width = 7;
cout<<r.area();
return 0;
}

