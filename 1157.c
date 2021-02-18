#include <stdio.h>
#include <string.h>

#define N 1000000

int main()
{
    char str[N + 1];
    int len;
    int cnt[26];
    int max;
    int max_idx;
    int max_flag;
    int i;
    
    scanf("%s", str);
    len = strlen(str);

    for (i = 0; i < 26; i++)
    {
        cnt[i] = 0;
    }

    for (i = 0; i < len; i++)
    {
        if ('a' <= str[i] && str[i] <= 'z')
        {
            cnt[str[i] - 'a']++;
        }
        else
        {
            cnt[str[i] - 'A']++;
        }
    }

    max = 0;
    max_flag = 0;
    for (i = 0; i < 26; i++)
    {
        if (max < cnt[i])
        {
            max = cnt[i];
            max_idx = i;
            max_flag = 0;
        }
        else if (max == cnt[i])
        {
            max_flag = 1;
        }
    }

    if (max_flag)
    {
        printf("?");
    }
    else
    {
        printf("%c", max_idx + 'A');
    }
    
    return 0;
}
