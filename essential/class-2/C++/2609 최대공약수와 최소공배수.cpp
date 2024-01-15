#include <iostream>

using namespace std;

int main(){
    int n, m, tmp, mini=0, maxi=0;
    cin >> n >> m;
    if (n > m) {
        tmp = n;
        n = m;
        m = tmp;
    }
    while(m%n!=0){
        tmp = n;
        n = m/n;
        m = tmp;
    }
    cout << n;
}