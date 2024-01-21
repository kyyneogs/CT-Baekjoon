#include <iostream>
#include <stack>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    while(1){
        int cnt=0;
        string s;
        stack<char> stack;
        getline(cin, s);
        if (s[0]=='.') break;

        for(int i=0; i<s.size(); i++){
            if (s[i]=='('||s[i]=='[') {
                stack.push(s[i]);
                cnt++;
            }
            else if (s[i]==')'||s[i]==']'){
                if (s[i]==')'&&!stack.empty()&&stack.top()=='(') stack.pop();
                else if (s[i]==']'&&!stack.empty()&&stack.top()=='[') stack.pop();
                cnt--;
            }
        }

        if (!cnt&&stack.empty()) cout << "yes\n";
        else cout << "no\n";
    }
}