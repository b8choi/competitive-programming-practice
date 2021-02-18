#include <stdio.h>

int main()
{
    int num;
    int count[42];
    int result;
    int i;

    for (i = 0; i <= 41; i++)
    {
        count[i] = 0;
    }

    result = 0;
    for (i = 0; i < 10; i++)
    {
        scanf("%d", &num);
        count[num % 42]++;
        if (count[num % 42] == 1)
        {
            result++;
        }
    }

    printf("%d", result);

    return 0;
}
