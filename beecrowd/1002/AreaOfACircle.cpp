#include <iostream>
#include <iomanip>
#include<cmath>
using namespace std;

int main(){
    double A, pi, result;
    pi = 3.14159;
    cin >> A;
    result = pi * pow(A, 2);
    cout << fixed << setprecision(4) << "A=" << result << endl;
    return 0;
}