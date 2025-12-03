#include <iostream>
#include <queue>

using namespace std;

int main() {
priority_queue<int> pq;
int x;

for ( int i=0;i < 5;i++) {
cin>>x;
pq.push(x);
}
while (!pq.empty()) {
cout<<pq.top()<<"";
pq.pop();
}
return 0;
}
