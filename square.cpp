#include <iostream>
using namespace std;
 
int square(int x) {
	return x*x;
}

int main() {
int number,sqr;
cout<< "Enter a number to square"<<endl;
cin>>number;
cout<<square(number)<<"Is the square"<<endl;
return 0;
}

