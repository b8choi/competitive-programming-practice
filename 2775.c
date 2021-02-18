#include <stdio.h>
#include <math.h>

#define N 14

int main()
{
    int t;
    int k, n;
    int i, j;
    int p[N + 1][N + 1];

    for (i = 0; i <= N; i++)
    {
        p[0][i] = i;
    }

    for (i = 1; i <= N; i++)
    {
        p[i][0] = 0;
        for (j = 1; j <= N; j++)
        {
            p[i][j] = p[i][j - 1] + p[i - 1][j];
        }
    }

    scanf("%d", &t);
    for (i = 0; i < t; i++)
    {
        scanf("%d %d", &k, &n);
        printf("%d\n", p[k][n]);
    }

    return 0;
}
