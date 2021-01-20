#include <stdio.h>
#include <string.h>

int main()
{
    int n;
    int m;
    int i, j;
    char ans[100];
    int score;
    int cnt;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%s", ans);
        m = strlen(ans);

        score = 0;
        cnt = 0;
        for (j = 0; j < m; j++)
        {
            if (ans[j] == 'O')
            {
                cnt++;
                score += cnt;
            }
            else
            {
                cnt = 0;
            }
        }

        printf("%d\n", score);
    }

    return 0;
}
