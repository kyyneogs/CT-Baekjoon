#include <iostream>

using namespace std;

int main(){
    int arr[42] = {0, }, T=10, i, cnt=0;

    while(T--){
        cin >> i;
        arr[i%42]++;
    }
    for(int j=0; j<42; j++){
        if (arr[j] > 0) cnt++;
    }
    cout << cnt;
}