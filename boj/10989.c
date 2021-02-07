#include <stdio.h>

#define MAX 10000

int main()
{
    int n;
    int cnt[MAX + 1] = {0, };
    int i, j;
    int m;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &m);
        cnt[m]++;
    }

    for (i = 1; i <= MAX; i++)
    {
        for (j = 0; j < cnt[i]; j++)
        {
            printf("%d\n", i);
        }
    }

    return 0;
}
