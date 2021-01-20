#include <stdio.h>

#define S 50

int main()
{
    int m, n;
    int i, j, k, l;
    char row[S];
    int b[S][S];
    int c[S][S];
    int sum;
    int min;

    scanf("%d %d", &m, &n);
    for (i = 0; i < m; i++)
    {
        scanf("%s", row);
        for (j = 0; j < n; j++)
        {
            b[i][j] = 0;
            if (row[j] == 'B')
            {
                b[i][j] = 1;
            }

            c[i][j] = 0;
            if (i % 2 == 0 && j % 2 == 0 || i % 2 == 1 && j % 2 == 1)
            {
                if (b[i][j] == 1)
                {
                    c[i][j] = 1;
                }
            }
            else
            {
                if (b[i][j] == 0)
                {
                    c[i][j] = 1;
                }
            }
        }
    }

    min = m * n;
    for (i = 0; i < m - 7; i++)
    {
        for (j = 0; j < n - 7; j++)
        {
            sum = 0;
            for (k = i; k < i + 8; k++)
            {
                for (l = j; l < j + 8; l++)
                {
                    sum += c[k][l];
                }
            }
            
            if (min > sum)
            {
                min = sum;
            }
            if (min > 8 * 8 - sum)
            {
                min = 8 * 8 - sum;
            }
        }
    }

    printf("%d", min);

    return 0;
}
