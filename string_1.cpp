#include <iostream>
#include <string>
using namespace std;

int main() {
string sentence;
cout<<"enter a sentence:"<<endl;
cin.ignore();
getline(cin,sentence);

cout<<"size of string is:"<<sentence.size();
return 0;
}
 
