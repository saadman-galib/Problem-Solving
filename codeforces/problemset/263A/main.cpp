#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    // Your code goes here
    int arr[5][5];

    int index[2];

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < 5; i ++){
        for (int j = 0; j < 5; j++){
            if(arr[i][j] == 1){
                index[0] = i;
                index[1] = j;
                break;
            }
        }
    }

    cout << abs(2 - index[0]) + abs(2 - index[1]) << endl;
    return 0;
}