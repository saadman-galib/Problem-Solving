#include<bits/stdc++.h>
using namespace std;

int main(){
    int number;
    double hour, earning, salary;
    cin >> number >> hour >> earning;
    salary = hour * earning;
    cout << "NUMBER = " << number << endl << "SALARY = U$ "<< fixed << setprecision(2) << salary << endl;
    return 0;
}