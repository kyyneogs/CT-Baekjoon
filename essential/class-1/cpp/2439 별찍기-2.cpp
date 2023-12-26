#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    for (int i=0; i<N; i++){
        for (int j=0; j+i+1<N; j++) cout << " ";
        for (int k=0; k<i+1; k++) cout << "*";
        cout << "\n";
    }
}