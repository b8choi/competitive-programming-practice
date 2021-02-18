#include <stdio.h>
#include <string.h>

#define N 10000

int d(int n)
{
    int diff;

    if (n < 10)
    {
        return 1;
    }

    diff = (n % 10) - ((n / 10) % 10);

    while (n / 10 > 0)
    {
        //printf("%d %d\n", (n % 10), ((n / 10) % 10));
        if ((n % 10) - ((n / 10) % 10) != diff)
        {
            return 0;
        }
        n /= 10;
    }

    return 1;
}

int main()
{
    int i;
    int n;
    int cnt = 0;

    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        if (d(i))
        {
            cnt++;
        }
    }

    printf("%d", cnt);

    return 0;
}
