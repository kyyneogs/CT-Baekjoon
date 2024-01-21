#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    vector<pair<int, int>> arr;
    int t, tc, sc[50];
    fill_n(sc, 50, 1);
    cin >> t;
    tc = t;
    while(tc--){
        int t1, t2;
        cin >> t1 >> t2;
        arr.push_back(make_pair(t1, t2));
    }
    for(int i=0; i<arr.size()-1; i++){
        for(int j=i+1; j<arr.size(); j++){
            if (arr[i].first > arr[j].first&&arr[i].second > arr[j].second) sc[j]++;
            else if (arr[i].first < arr[j].first&&arr[i].second < arr[j].second) sc[i]++;
        }
    }
    for (int i=0; i<t; i++) cout << sc[i] << " ";
}