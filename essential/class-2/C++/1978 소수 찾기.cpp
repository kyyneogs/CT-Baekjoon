#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n, cnt;
    cin >> n;
    cnt = n;
    while(n--){
        int t;
        cin >> t;
        if (t==1) cnt--;

        for (int i=2; i<=(int)pow(t, 0.5); i++){
            if (t%i==0){
                cnt--;
                break;
            }
        }
    }
    cout << cnt;
}