#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;

    while(T--){
        int H, W, N, f, b;
        cin >> H >> W >> N;

        b = (N-1) / H + 1;
        f = (N-1) % H + 1;

        cout << f*100 + b << endl;
    }
}