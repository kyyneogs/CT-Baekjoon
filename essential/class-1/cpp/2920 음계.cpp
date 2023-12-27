#include <iostream>

using namespace std;

int main(){
    int arr[8] = {0, };

    for (int i=0; i<8; i++) cin >> arr[i];
    int flag = arr[0];

    for (int i=1; i<8; i++){
        if ((flag == 8 and arr[i-1] < arr[i]) or (flag==1 and arr[i-1] > arr[i])){
            flag = -1;
            break;
        }
    }

    switch (flag){
        case 1:
            cout << "ascending";
            break;
        case 8:
            cout << "descending";
            break;
        default:
            cout << "mixed";
            break;
    }
}