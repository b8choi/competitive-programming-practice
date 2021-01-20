#include <stdio.h>

#define N 1000

int main()
{
    int n;
    int nums[N];
    int max;
    double sum;
    int i;

    scanf("%d", &n);
    max = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &nums[i]);
        if (max < nums[i])
        {
            max = nums[i];
        }
    }

    for (i = 0; i < n; i++)
    {
        sum += ((double)nums[i] / max) * 100;
    }

    printf("%.2lf", sum / n);

    return 0;
}
