#include <iostream>

int main(){
    int t, n=0;
    for(;std::cin >> t;) n = 10*n + t;
    std::cout << (n == 12345678 ? "ascending" : (n == 87654321 ? "descending" : "mixed"));
}