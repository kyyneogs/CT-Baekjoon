#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

vector<string> split(string input, char deli){
    vector<string> result;
    stringstream ss(input);
    string buff;

    while(getline(ss, buff, deli)){
        if (!(buff == "")){
            result.push_back(buff);
        }
    }

    return result;
}

int main(){
    string input;
    getline(cin, input);

    vector<string> answer = split(input, ' ');

    cout << answer.size();
}