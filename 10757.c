#include <stdio.h>
#include <string.h>

#define D 10000

char a[D + 1];
char b[D + 1];

int main()
{
    int n;
    int len_a;
    int len_b;
    int len_m;
    int len_s;
    int i;
    char tmp;

    scanf("%s %s", a, b);
    len_a = strlen(a);
    len_b = strlen(b);

    for (i = 0; i < len_a; i++)
    {
        a[i] -= '0';
    }
    for (i = 0; i < len_b; i++)
    {
        b[i] -= '0';
    }

    for (i = 0; i < len_a / 2; i++)
    {
        tmp = a[i];
        a[i] = a[len_a - i - 1];
        a[len_a - i - 1] = tmp;
    }
    for (i = 0; i < len_b / 2; i++)
    {
        tmp = b[i];
        b[i] = b[len_b - i - 1];
        b[len_b - i - 1] = tmp;
    }

    len_m = len_a;
    if (len_m < len_b)
    {
        len_m = len_b;
    }

    for (i = 0; i < len_m + 1; i++)
    {
        a[i] += b[i];
        a[i + 1] += a[i] / 10;
        a[i] = a[i] % 10;
        //printf("%d ", a[i]);
    }

    len_s = len_m;
    if (a[len_m] > 0)
    {
        len_s = len_m + 1;
    }

    for (i = len_s - 1; i >= 0; i--)
    {
        printf("%d", a[i]);
    }

    return 0;
}
