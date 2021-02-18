#include <stdio.h>
#include <string.h>

#define N 15

int main()
{
    char str[N + 1];
    int n;
    int sum;
    int i;

    scanf("%s", str);
    n = strlen(str);

    sum = 0;
    for (i = 0; i < n; i++)
    {
        if (str[i] <= 'C')
        {
            sum += 3;
        }
        else if (str[i] <= 'F')
        {
            sum += 4;
        }
        else if (str[i] <= 'I')
        {
            sum += 5;
        }
        else if (str[i] <= 'L')
        {
            sum += 6;
        }
        else if (str[i] <= 'O')
        {
            sum += 7;
        }
        else if (str[i] <= 'S')
        {
            sum += 8;
        }
        else if (str[i] <= 'V')
        {
            sum += 9;
        }
        else if (str[i] <= 'Z')
        {
            sum += 10;
        }
    }

    printf("%d", sum);

    return 0;
}
