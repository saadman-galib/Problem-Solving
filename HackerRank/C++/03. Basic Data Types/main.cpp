#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int num;
	long longnum;
	char character;
	float floatnum;
	double doublenum;
	num = 3;
	longnum = 12345678912345;
	character = 'a';
	floatnum = 334.23;
	doublenum = 14049.30493;
	scanf("%d %ld %c %f %lf", &num, &longnum, &character, &floatnum, &doublenum);
	printf("%d\n%ld\n%c\n%f\n%lf\n", num, longnum, character, floatnum, doublenum);
	return 0;
}
