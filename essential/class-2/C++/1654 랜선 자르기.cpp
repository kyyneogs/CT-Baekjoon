#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int K, N;
    cin >> K >> N;

    unsigned arr[K], left=1, right=0;
    
    for (int i=0; i<K; i++) {
        cin >> arr[i];
        if (right < arr[i]) right = arr[i];
    }

    while(left <= right){
        unsigned cnt=0, mid = (left+right)/2;
        for (int i=0; i<K; i++) cnt += arr[i]/mid;

        if (cnt >= N) left = mid+1;
        else right = mid-1;
    }
    cout << right;
}