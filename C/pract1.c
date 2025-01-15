#include<stdio.h>

int main(){
    enum Snames { Teja, Ravi, RAM };
    enum Snames s1;
    s1 = Ravi;
    printf("%d", s1);
    return 0;
}