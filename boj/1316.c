#include <stdio.h>
#include <string.h>

#define S 100

char checker(char *str)
{
    int len;
    int flag[26];
    int i;

    len = strlen(str);

    for (i = 0; i < 26; i++)
    {
        flag[i] = 0;
    }
    
    for (i = 0; i < len; i++)
    {
        if (i == 0 || (str[i] != str[i - 1] && flag[str[i] - 'a'] == 0))
        {
            flag[str[i] - 'a'] = 1;
        }
        else if (i > 0 && str[i] != str[i - 1] && flag[str[i] - 'a'] == 1)
        {
            return 0;
        }
    }

    return 1;
}

int main()
{
    int n;
    char str[S + 1];
    int len;
    int cnt;
    int i;

    scanf("%d", &n);
    cnt = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%s", str);
        if (checker(str) == 1)
        {
            cnt++;
        }
    }

    printf("%d", cnt);

    return 0;
}
