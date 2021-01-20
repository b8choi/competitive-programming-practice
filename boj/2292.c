#include <stdio.h>

int main()
{
    int n;
    int sum;
    int i;

    scanf("%d", &n);

    sum = 1;
    for (i = 0; ; i++)
    {
        sum += i * 6;
        if (sum >= n)
        {
            printf("%d", i + 1);
            break;
        }
    }

    return 0;
}
