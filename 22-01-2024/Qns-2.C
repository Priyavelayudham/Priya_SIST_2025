//count
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    long long num;
    int count=0;
    scanf("%lld",&num);
    do
    {
        num=num/10;
        ++count;
    }while(num!=0);
    printf("%d",count);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
