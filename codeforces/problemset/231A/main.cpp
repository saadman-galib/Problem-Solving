#include <iostream>
using namespace std;

int main() {
    // Your code goes here
    int t;
    int total = 0;

    cin >> t;

    while(t--){
        int a, b, c;

        cin >> a >> b >> c;

        total += ((a + b + c > 1) ? 1 : 0);
    }

    cout << total << endl;

    return 0;
}