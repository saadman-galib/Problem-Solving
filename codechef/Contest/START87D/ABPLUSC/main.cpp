#include <bits/stdc++.h> // include all standard headers
using namespace std;

#define ll long long
#define ld long double
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define fi first
#define se second

const int INF = 1e9;
const ll INFLL = 1e18;
const int MOD = 1e9 + 7;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // Declare any additional variables here
    
    int t; // number of test cases
    cin >> t;
    
    while (t--) {
        // write your code here for each test case
        int x, a, b, c;
        a = b = c = 1;
        
        cin >> x;
        int y = x;

        if (x > 1000000){
            y = 1000000;
        }
        if(x > 1){
            for(int i = 1; i < y; i++){ // c
                for(int j = 1; j < y; j++){ // a
                    for(int k = 1; k < y; k++){ // b
                        if(j * k + i == x){
                            a = j;
                            b = k;
                            c = i;
                            break;
                        }
                    }
                    break;
                }
                break;
            }
            cout << a << " " << b << " " << c << endl;
        }
        else{
            cout << -1 << endl;
        }
    }
    return 0;
}

# not solved