#include <iostream>
#include <string>

using namespace std;

int main(){
    int i=665, cnt=0, N;
    cin >> N;

    while(cnt != N){
        string s = to_string(++i);
        if (s.find("666") != string::npos) cnt++;
    }

    cout << i;
}