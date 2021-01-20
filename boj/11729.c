#include <stdio.h>

#define MAX 1100000

int n;
int cnt;
int mov[MAX][2];

void hanoi(int n, int s, int m, int t)
{
    if (n == 0)
    {
        return;
    }

    hanoi(n - 1, s, t, m);
    mov[cnt][0] = s;
    mov[cnt][1] = t;
    cnt++;
    hanoi(n - 1, m, s, t);
}

int main()
{
    int i;

    scanf("%d", &n);

    cnt = 0;
    hanoi(n, 1, 2, 3);

    printf("%d\n", cnt);
    for (i = 0; i < cnt; i++)
    {
        printf("%d %d\n", mov[i][0], mov[i][1]);
    }

    return 0;
}
