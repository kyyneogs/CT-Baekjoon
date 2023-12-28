#include <iostream>

using namespace std;

string solution[8] = {
    "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M, mini=999;
    cin >> N >> M;

    string board[N];
    for (int i=0; i<N; i++) cin >> board[i];

    for (int x=0; x<=N-8; x++){
        for (int y=0; y<=M-8; y++){
            int t1=0, t2=0;
            for (int i=x; i<x+8; i++){
                for (int j=y; j<y+8; j++){
                    if (board[i][j] == solution[i-x][j-y]) t1++;
                    else t2++;
                }
            }
            mini = min(t2, min(t1, mini));
        }
    }
    cout << mini;
}