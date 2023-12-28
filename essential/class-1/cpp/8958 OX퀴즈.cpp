#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;

    while(T--){
        int result = 0, cnt = 0;
        string input;
        cin >> input;

        for(int i=0; i<input.length(); i++){
            if (input[i] == 'O') result += ++cnt;
            else cnt = 0;
        }
        cout << result << endl;
    }
}