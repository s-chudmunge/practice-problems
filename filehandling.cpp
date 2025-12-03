#include <iostream>
#include <fstream>

using namespace std;

int main() {
ofstream out("note.txt");
out<<"Hi! my name is Sankalp and this program reads and writes from a file";
out.close();

ifstream in("note.txt");
string line;
getline(in,line);
cout<<line;
in.close();

return 0;
}
