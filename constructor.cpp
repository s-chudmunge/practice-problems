#include <iostream>

using namespace std;
class student{
public:
	string name;
	int age;
	
	student(string n,int a){
		name=n;
		age=a;
	}
};

int main() {
student s("Rahul",20);
cout << s.name << " is " << s.age << " years old!" << endl;
return 0;
}
