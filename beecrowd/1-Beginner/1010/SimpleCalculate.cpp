#include<bits/stdc++.h>
using namespace std;

int main(){
    int p1, p2, u1, u2;
    double price1, price2;

    cin >> p1 >> u1 >> price1;
    cin >> p2 >> u2 >> price2;

    cout << "VALOR A PAGAR: R$ " << fixed << setprecision(2) << (u1 * price1) + (u2 * price2) << endl;
    return 0;
}