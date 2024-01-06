#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n, t, sumi=0;
    int mid, maxi=-4001, mini=4001, freq[8001]={0, };
    cin >> n;
    t = n;

    while(t--){
        int k;
        cin >> k;
        sumi += k;
        freq[k]++;

        if (maxi < k) maxi = k;
        if (mini > k) mini = k;
        if (t==n/2) mid = k;
    }

    cout << round(sumi/n) << "\n";
    cout << mid << "\n";
}