#include <stdio.h>

#define N 50

int main()
{
    int n;
    int w[N];
    int h[N];
    int i, j;
    int rank;
    int a, b;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d %d", &w[i], &h[i]);
    }

    for (i = 0; i < n; i++)
    {
        rank = 1;
        for (j = 0; j < n; j++)
        {
            if (w[i] < w[j] && h[i] < h[j])
            {
                rank++;
            }
        }

        printf("%d ", rank);
    }

    return 0;
}
