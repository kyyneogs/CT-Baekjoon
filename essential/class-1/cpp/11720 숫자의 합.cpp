#include <iostream>

using namespace std;

int main(){
    int N, sumi=0;
    string input;

    cin >> N >> input;

    for (int i=0; i<N; i++) sumi += (int)input[i]-48;

    cout << sumi;
}