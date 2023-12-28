#include <iostream>

using namespace std;

int main(){
    int arr[26];
    fill_n(arr, 26, -1); // 원하는 값으로 배열 초기화.
    string input;
    cin >> input;

    for (int i=0; i<input.length(); i++){
        int j = int(input[i])-97;
        if (arr[j] == -1) arr[j] = i;
    }

    for (int i=0; i< 26; i++) cout << arr[i] << " ";
}