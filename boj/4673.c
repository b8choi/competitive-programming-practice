#include <stdio.h>
#include <string.h>

#define N 10000

int d(int n)
{
    int sum = n;

    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }

    return sum;
}

int main()
{
    int i, j;
    int flag;

    for (i = 1; i <= N; i++)
    {
        flag = 0;
        for (j = 1; j < i; j++)
        {
            if (d(j) == i)
            {
                flag = 1;
                break;
            }
        }

        if (flag == 0)
        {
            printf("%d\n", i);
        }
    }

    return 0;
}
