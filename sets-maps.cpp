#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
int main() {
unordered_map<string, int> mp;
mp["india"] = 91;
mp["usa"] = 1;
mp["azerbaijan"]=994;
string country;
cin>>country;
cout<<"Code for this country is:"<<mp[country]<<endl;
return 0;
}
