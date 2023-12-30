#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int N, K=0;
    cin >> N;

    stack<int> stack;
    vector<char> answer;

    while(N--){
        int t;
        cin >> t;

        if (!stack.empty() && stack.top() > t) break;
        
        while(K < t){
            stack.push(++K);
            answer.push_back('+');
        }

        while(!stack.empty() && stack.top() >= t){
            stack.pop();
            answer.push_back('-');
        }
    }
    if (stack.empty()) for (int i=0; i<answer.size(); i++) cout << answer[i] << '\n';
    else cout << "NO";
}