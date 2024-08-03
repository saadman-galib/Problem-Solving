#include <iostream>
using namespace std;

int main() {
    // Your code goes here
    string a, b;
    cin >> a >> b;

    for (int i = 0; i < a.length(); i++){
        if(a[i] < 92){
            a[i] += 32;
        }

        if(b[i] < 92){
            b[i] += 32;
        }
    }

    if(a < b){
        cout << -1 << endl;
    }
    else if(b < a){
        cout << 1 << endl;
    }
    else{
        cout << 0 << endl;
    }

    return 0;
}