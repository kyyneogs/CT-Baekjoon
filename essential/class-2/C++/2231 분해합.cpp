#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n;

    cin >> n;
    
    for (int i=(int)sqrt(n); i <= n; i++){
        int t=i, result=i;
        while(t!=0){
            result += t%10;
            t /= 10;
        }
        if (result == n){
            cout << i;
            return 0;
        }
    }

    cout << "0";
    return 0;
}