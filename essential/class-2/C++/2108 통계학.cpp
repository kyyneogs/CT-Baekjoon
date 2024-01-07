#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    vector<int> stack;
    int n, t, sumi=0;
    int freqMax=0, freqCnt=0, freqIdx;
    int maxi=-8000, mini=8000, freq[8001]={0, };
    cin >> n;
    t = n;

    while(t--){
        int k;
        cin >> k;
        stack.push_back(k);
        sumi += k;
        freq[k+4000]++;

        if (maxi < k) maxi = k;
        if (mini > k) mini = k;
    }
    for (int i=mini+4000; i<= maxi+4000; i++){
        if (freq[i] > freqMax) {
            freqMax = freq[i];
            freqCnt = 0;
            freqIdx = i;
        }
        else if (freq[i] == freqMax) {
            freqCnt++;
            if (freqCnt == 1) freqIdx = i;
        }
    }
    sort(stack.begin(), stack.end());

    double avg = sumi / (double)n;
    cout << (int)round(avg) << "\n";
    cout << stack[(n-1)/2] << "\n";
    cout << freqIdx-4000 << "\n";
    cout << maxi - mini;
    }