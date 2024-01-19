#include <iostream>

using namespace std;

int main(){
    int a, b, v, d;
    cin >> a >> b >> v;
    v -= a;
    d = v/(a-b)+1;
    if (v%(a-b)!=0) d++;
    cout << d;
}