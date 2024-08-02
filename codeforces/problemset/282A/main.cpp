#include <iostream>
using namespace std;

int main() {
    // Your code goes here
    int n;
    cin >> n;

    int total = 0;
    
    while(n--){
        string s;
        cin >> s;

        if(s == "X++" or s == "++X"){
            total += 1;
        }
        else{
            total -= 1;
        }
    }

    cout << total << endl;
    return 0;
}