#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int T;
    cin >> T;

    while(T--){
        int N, M, cnt=0;
        queue<pair<int, int>> que;

        cin >> N >> M;
        int *priority = new int[N];

        for (int i=0; i<N; i++) {
            int t;
            cin >> t;
            que.push({i, t});
            priority[i] = t;
        }

        sort(priority, priority+N, greater<>());

        while(!que.empty()){
            int idx = que.front().first, pri = que.front().second;
            que.pop();

            if (pri == priority[cnt]){
                cnt++;
                if (idx == M) break;
            }
            else que.push({idx, pri});
        }
        cout << cnt << "\n";
        delete []priority;
    }
}