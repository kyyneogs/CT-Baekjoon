#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int n, m, sumi, maxi=0;
    cin >> n >> m;

    int card[300000] = {0,};
    for (int i=0; i<n; i++) cin >> card[i];
    for (int i=0; i<n-2; i++){
        for (int j=i+1; j<n-1; j++){
            for (int k=j+1; k<n; k++){
                sumi = card[i]+card[j]+card[k];
                if (sumi <= m && sumi > maxi) maxi = sumi;
            }
        }
    }
    cout << maxi;
}