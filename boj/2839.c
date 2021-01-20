#include <stdio.h>

int main()
{
    int n;
    int a, b;
    int i, j;

    scanf("%d", &n);

    a = n / 5;
    b = n / 3;

    for (i = a; i >= 0; i--)
    {
        for (j = 0; j <= n; j++)
        {
            if (i * 5 + j * 3 == n)
            {
                printf("%d", i + j);

                return 0;
            }
        }
    }

    printf("-1");

    return 0;
}
