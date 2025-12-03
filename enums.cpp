#include <iostream>

using namespace std;

enum class Level { Low=0,Medium=1,High=2 };
int main() {
int n;
cin>>n;
if (n < 0 || n > 2) {
    cout << "Invalid";
    return 0;
}

Level lvl = Level(n);

if(lvl == Level::Low) cout<<"Low";
else if (lvl == Level::Medium) cout<<"Medium";
else cout<< "High";

return 0;
}


