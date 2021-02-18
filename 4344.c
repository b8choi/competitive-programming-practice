#include <stdio.h>
#include <string.h>

#define M 1000

int main()
{
    int n;
    int m;
    int score[M];
    int sum;
    double avg;
    int cnt;
    int i, j;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &m);

        sum = 0;
        for (j = 0; j < m; j++)
        {
            scanf("%d", &score[j]);
            sum += score[j];
        }
        avg = (double)sum / m;

        cnt = 0;
        for (j = 0; j < m; j++)
        {
            if (score[j] > avg)
            {
                cnt++;
            }
        }

        printf("%.3lf%%\n", ((double)cnt / m) * 100);
    }

    return 0;
}
