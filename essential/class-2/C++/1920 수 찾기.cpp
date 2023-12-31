#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N, M;
    cin >> N;

    long int arr[N];
    for (int i=0; i<N; i++) cin >> arr[i];
    sort(arr, arr+N);

    cin >> M;
    while(M--){
        int left=0, right=N-1, mid, ans=0;
        long int t;
        cin >> t;

        while(left <= right){
            mid = (left+right)/2;
            if (arr[mid] > t) right = mid-1;
            else if (arr[mid] < t) left = mid+1;
            else {
                ans = 1;
                break;
            }
        }
        cout << ans << "\n";
    }
}