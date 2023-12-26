#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int arr[10] = {0, }, A, B, C;
    cin >> A >> B >> C;
    string s = to_string(A*B*C);

    for (int i=0; i<s.length(); i++) {
        arr[s[i]-48]++;
    }
    
    for (int i=0; i<10; i++) cout << arr[i] << "\n";
}