#include <stdio.h>
#include <math.h>

int main()
{
    int m;
    int i;
    int h, w, n;
    int x, y;

    scanf("%d", &m);
    for (i = 0; i < m; i++)
    {
        scanf("%d %d %d", &h, &w, &n);

        x = ceil((double)n / h);
        y = n - ((x - 1) * h);

        printf("%d", y);
        if (x < 10)
        {
            printf("0");
        }
        printf("%d\n", x);
    }

    return 0;
}
