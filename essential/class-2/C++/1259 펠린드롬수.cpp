#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    string T;
    while (1){
        cin >> T;
        if (T == "0") break;

        int st = T.length()%2 == 0 ? T.length()/2 : T.length()/2+1;

        string left = T.substr(0, T.length()/2);
        string right = T.substr(st, T.length());

        reverse(right.begin(), right.end());

        if (left == right) cout << "yes" << "\n";
        else cout << "no" << "\n";
    }
}