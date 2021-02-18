#include <stdio.h>
#include <math.h>

int main()
{
    int t;
    int x, y;
    int d;
    int s;
    int sum[100000];
    int i, j;

    s = 0;
    for (i = 1; ; i++)
    {
        s += i;
        sum[i] = s * 2 - i;
        if (s * 2 - i <= 0)
        {
            break;
        }
    }

    scanf("%d", &t);
    for (i = 0; i < t; i++)
    {
        scanf("%d %d", &x, &y);
        d = y - x;

        for (j = 1; ; j++)
        {
            if (sum[j] == d)
            {
                printf("%d", j * 2 - 1);
                break;
            }
            else if (sum[j + 1] <= 0 || sum[j + 1] > d)
            {
                if (d - sum[j] > j)
                {
                    printf("%d", j * 2 + 1);
                }
                else
                {
                    printf("%d", j * 2);
                }

                break;
            }
        }
        printf("\n");
    }

    return 0;
}
