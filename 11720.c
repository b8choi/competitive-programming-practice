#include <stdio.h>
#include <string.h>

#define N 100

int main()
{
    char str[N + 1];
    int n;
    int i;
    int idx[26];
    
    scanf("%s", str);
    n = strlen(str);

    for (i = 0; i < 26; i++)
    {
        idx[i] = -1;
    }

    for (i = n - 1; i >= 0; i--)
    {
        idx[str[i] - 'a'] = i;
    }

    for (i = 0; i < 26; i++)
    {
        printf("%d ", idx[i]);
    }
    
    return 0;
}
