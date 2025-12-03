#include <iostream>
using namespace std;

class Shape {
public:
	virtual void draw() = 0;	
};

class Square : public Shape {
public:
     void draw() override {
		cout<< "Drawing a square";
	}
};

int main() {
Shape* a=new Square();
a->draw();
}

