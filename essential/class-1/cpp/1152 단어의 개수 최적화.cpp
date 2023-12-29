#include <iostream>

using namespace std;

int main(){
    string input;
    int cnt = 0;
    getline(cin, input);

    if (input[0] != ' ') cnt++;
    for (int i=0; i<input.length(); i++) if (input[i-1] == ' ' && input[i] != ' ') cnt++;

    cout << cnt;
}