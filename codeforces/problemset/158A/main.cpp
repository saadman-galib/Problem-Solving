#include <iostream>
using namespace std;

int main() {
    // Your code goes here
    int n, k;
    cin >> n >> k;

    int arr[n];

    int total = 0;

    for (int i = 0; i < n; i++) {
        cin >> arr[i]; 
    }

    for (int i = 0; i < n; i++) {
        total += (arr[i] != 0 && arr[i] >= arr[k - 1]) ? 1 : 0;
    }

    cout << total << endl;
    return 0;
}