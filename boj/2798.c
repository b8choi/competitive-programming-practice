#include <stdio.h>

#define N 100

int main()
{
    int n, m;
    int nums[N];
    int i, j, k;
    int sum;
    int max;

    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &nums[i]);
    }

    max = 0;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (j != i)
            {
                for (k = 0; k < n; k++)
                {
                    if (k != i && k != j)
                    {
                        sum = nums[i] + nums[j] + nums[k];
                        if (sum <= m && max < sum)
                        {
                            max = sum;
                        }
                    }
                }
            }
        }
    }

    printf("%d", max);

    return 0;
}
