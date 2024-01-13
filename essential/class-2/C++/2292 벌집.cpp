#include <iostream>

using namespace std;

int main(){
    int N, result=1;
    cin >> N;
    N -= 2;

    if (N>-1) {
        int i=0, j=1;
        N /= 6;
        while(i<=N){
            i += j++;
            result++;
        }
    }
    cout << result;
}