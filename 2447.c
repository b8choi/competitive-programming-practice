#include <stdio.h>

#define N 2187

int map[N + 1][N + 1];

int star(int x, int y, int size)
{
    int i, j;

    if (size == 1)
    {
        map[y][x] = 1;
    }
    else
    {
        size /= 3;
        star(x + 0, y + 0, size);
        star(x + 0, y + size * 1, size);
        star(x + 0, y + size * 2, size);
        star(x + size * 1, y + 0, size);
        star(x + size * 1, y + size * 2, size);
        star(x + size * 2, y + 0, size);
        star(x + size * 2, y + size * 1, size);
        star(x + size * 2, y + size * 2, size);
    }
}

int main()
{
    int n;
    int i, j;

    scanf("%d", &n);

    star(0, 0, n);

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (map[i][j] == 1)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}
