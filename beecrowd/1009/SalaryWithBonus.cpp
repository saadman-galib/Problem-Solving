#include<bits/stdc++.h>
using namespace std;

int main(){
    string name;
    double salary, sold, soldPercentage, finalSalary;
    cin >> name >> salary >> sold;
    soldPercentage = sold * 0.15;
    finalSalary = salary + soldPercentage;
    cout << "TOTAL = R$ " << fixed << setprecision(2) << finalSalary << endl;
    return 0;
}