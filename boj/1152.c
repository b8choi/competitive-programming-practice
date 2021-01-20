#include <stdio.h>
#include <string.h>

#define N 1000000

int main()
{
    char str[N + 1];
    int len;
    int cnt;
    int i;

    gets(str);
    len = strlen(str);
    
    cnt = 1;
    for (i = 0; i < len; i++)
    {
        if (str[i] == ' ')
        {
            cnt++;
        }
    }

    if (str[0] == ' ')
    {
        cnt--;
    }
    if (str[len - 1] == ' ')
    {
        cnt--;
    }
    printf("%d", cnt);
    
    return 0;
}
