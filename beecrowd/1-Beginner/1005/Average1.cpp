#include<bits/stdc++.h>
using namespace std;

int main(){
    float A, B, M;
    cin >> A >> B;
    A = A * 3.5;
    B = B * 7.5;
    M = (A + B) / (3.5 + 7.5);
    cout << "MEDIA = " << fixed << setprecision(5) << M << endl;
    return 0;
}