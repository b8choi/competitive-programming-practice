#include <stdio.h>
#include <math.h>

int main()
{
    int a, b, v;
    double d;

    scanf("%d %d %d", &a, &b, &v);

    d = ceil((double)(v - a) / (a - b));
    printf("%d\n", (int)d + 1);

    return 0;
}
