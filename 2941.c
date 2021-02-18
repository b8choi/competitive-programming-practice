#include <stdio.h>
#include <string.h>

#define N 100

int main()
{
    char str[N + 1];
    int n;
    int cnt;
    int i;
    int diff = 0;

    scanf("%s", str);
    n = strlen(str);

    for (i = 0; i < n; i++)
    {
        if (i > 0)
        {
            if (str[i] == '-')
            {
                if (str[i - 1] == 'c' || str[i - 1] == 'd')
                {
                    diff++;
                }
            }
            else if (str[i] == '=')
            {
                if (str[i - 1] == 'c' || str[i - 1] == 's')
                {
                    diff++;
                }
                else if (str[i - 1] == 'z')
                {
                    diff++;
                    if (i > 1 && str[i - 2] == 'd')
                    {
                        diff++;
                    }
                }
            }
            else if (str[i] == 'j')
            {
                if (str[i - 1] == 'l' || str[i - 1] == 'n')
                {
                    diff++;
                }
            }
        }
    }

    printf("%d", n - diff);

    return 0;
}
