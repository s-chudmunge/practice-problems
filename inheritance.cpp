#include <iostream>
using namespace std;

class Vehicle {
public:
    void start() { cout << "Starting...\n"; }
};

class Car : public Vehicle {
public:
    void honk() { cout << "Beep!\n"; }
};

int main() {
Car car;
car.honk();
car.start();
return 0;
}
