#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    int arr[N], maxi, mini;
    for (int i=0; i<N; i++) cin >> arr[i];

    maxi = arr[0]; mini = arr[0];

    for (int i=1; i<N; i++){
        if (arr[i] > maxi) maxi = arr[i];
        else if (arr[i] < mini) mini = arr[i];
    }

    cout << mini << " " << maxi;
}