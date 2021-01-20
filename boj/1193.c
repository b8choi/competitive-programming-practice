#include <stdio.h>

int main()
{
    int n;
    int i;
    int sum;
    int offset;
    int x, y;

    scanf("%d", &n);

    sum = 0;
    for (i = 1; ; i++)
    {
        sum += i;
        if (sum >= n)
        {
            offset = n - (sum - i) - 1;
            if (i % 2 != 0)
            {
                x = 1 + offset;
                y = i - offset;
            }
            else
            {
                x = i - offset;
                y = 1 + offset;
            }

            break;
        }
    }

    printf("%d/%d", y, x);

    return 0;
}
