#include <stdio.h>
#include <string.h>

#define N 100

int main()
{
    int n;
    int r;
    char str[N + 1];
    int len;
    int i, j, k;
    
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d %s", &r, str);
        len = strlen(str);

        for (j = 0; j < len; j++)
        {
            for (k = 0; k < r; k++)
            {
                printf("%c", str[j]);
            }
        }
        printf("\n");
    }
    
    return 0;
}
