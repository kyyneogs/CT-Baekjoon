#include <iostream>

using namespace std;

int main(){
    int arr[26] = {0, }, maxi = 0, midx = 0;
    string input;
    cin >> input;
    
    for (int i=0; i<input.length(); i++){
        int c = input[i];
        c = (c < 97) ? c-65 : c-97;
        arr[c]++;
    }

    int tcnt = 0;

    for (int i=0; i<26; i++){
        if (maxi < arr[i]){
            midx = i;
            maxi = arr[i];
            tcnt = 0;
        }
        else if (maxi == arr[i]) {
            tcnt++;
        }
    }

    if (tcnt==0) cout << char(midx+65);
    else cout << "?";
}