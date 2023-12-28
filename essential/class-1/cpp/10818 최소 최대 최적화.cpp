#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, t, maxi, mini;
    cin >> N >> t;

    maxi = t; mini = t;

    for (int i=1; i<N; i++){
        cin >> t;
        maxi = maxi > t ? maxi : t;
        mini = mini < t ? mini : t;
    }

    cout << mini << " " << maxi;
}