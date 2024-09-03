#include <bits/stdc++.h>
using namespace std;

int main() {

    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;

        for (int i = 0; i < n; i++) {
            string s;
            cin >> s;
            for (int j = 0; j < 4; j++) {
                if (s[j] == '#') {
                    cout << j + 1 << " ";
                    break;
                }
            }
        }
        cout << endl;
        
    }
    
    return 0;
}

// Not solved