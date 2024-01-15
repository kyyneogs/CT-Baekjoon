#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int t, k, n, arr[15][15] = {0, };
    cin >> t;

    for (int i=1; i<15; i++) arr[0][i] = arr[0][i-1]+i;
    for (int i=1; i<15; i++){
        for (int j=1; j<15; j++) arr[i][j] = arr[i][j-1]+arr[i-1][j];
    }
    while(t--){
        cin >> k >> n;
        cout << arr[k][n] - arr[k][n-1] << "\n";
    }
}