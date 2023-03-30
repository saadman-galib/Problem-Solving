#include<bits/stdc++.h>
using namespace std;

int main(){
    float A, B, C, M;
    cin >> A >> B >> C;
    A = A * 2;
    B = B * 3;
    C = C * 5;
    M = (A + B + C) / (2 + 3 + 5);
    cout << "MEDIA = " << fixed << setprecision(1) << M << endl;
    return 0;
}