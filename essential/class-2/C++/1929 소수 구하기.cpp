#include <iostream>
#include <cmath>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int M, N;
    cin >> M >> N;
    int *arr = new int[N+1]();
    arr[1] = 1;

    for(int i=2; i<=(int)pow(N, 0.5); i++){
        int j=i*2;
        while(j <= N){
            arr[j]++;
            j += i;
        }
    }
    for (int i=M; i<=N; i++){
        if (!arr[i]) cout << i << "\n";
    }
    delete []arr;
}