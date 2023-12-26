#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;

    while(T-- > 0){
        int r;
        string s;

        cin >> r >> s;
        for (int i=0; i<s.length(); i++){
            for (int j=0; j<r; j++){
                cout << s[i];
            }
        }
        cout << endl;
    }
}