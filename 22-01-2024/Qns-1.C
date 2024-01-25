//reverse number
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int num,digits,rev=0;
    scanf("%d",&num);
    while(num!=0)
    {
        digits=num%10;
        rev=rev*10+digits;
        num=num/10;
    }
    printf("%d",rev);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
