#include <iostream>
#include <algorithm>

using namespace std;

bool cmp(string a, string b){
    if (a.length() == b.length()) return a < b;
    else return a.length() < b.length();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N;
    cin >> N;

    string arr[N];
    for (int i=0; i<N; i++) cin >> arr[i];
    sort(arr, arr+N, cmp);
    for (int i=0; i<N; i++) {
        if (arr[i] == arr[i-1]) continue;
        cout << arr[i] << "\n";
    }
}