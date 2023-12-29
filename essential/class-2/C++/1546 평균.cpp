#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    int t, maxi = 0, sumi = 0;
    for (int i=0; i<N; i++) {
        cin >> t;
        sumi += t;
        maxi = maxi > t ? maxi : t;
    }

    cout << (double)(sumi*100/maxi)/N;
}