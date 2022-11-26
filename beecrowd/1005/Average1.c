#include<stdio.h>

int main(){
    float A, B, M;
    scanf("%f\n%f", &A, &B);
    A = A * 3.5;
    B = B * 7.5;
    M = (A + B) / (3.5 + 7.5);
    printf("MEDIA = %.5f\n", M);
    return 0;
}