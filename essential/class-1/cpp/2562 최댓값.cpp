#include <iostream>

using namespace std;

int main(){
    int maxi = 0, idx = 0;

    for (int i=0; i<9; i++){
        int input;
        cin >> input;
        if (maxi < input){
            maxi = input;
            idx = i+1;
        }
    }
    cout << maxi << "\n" << idx;
}