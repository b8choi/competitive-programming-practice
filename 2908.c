#include <stdio.h>

int main()
{
    char a[4];
    char b[4];
    int x, y;

    scanf("%s %s", a, b);

    x = (a[2] - '0') * 100 + (a[1] - '0') * 10 + (a[0] - '0');
    y = (b[2] - '0') * 100 + (b[1] - '0') * 10 + (b[0] - '0');

    if (x > y)
    {
        printf("%d", x);
    }
    else
    {
        printf("%d", y);
    }

    return 0;
}
