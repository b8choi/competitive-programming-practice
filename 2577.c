#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a, b, c;
    int result;
    char nums[100];
    int n;
    int count[10];
    int i;

    scanf("%d %d %d", &a, &b, &c);

    result = a * b * c;
    sprintf(nums, "%d", result);
    n = strlen(nums);

    for (i = 0; i <= 9; i++)
    {
        count[i] = 0;
    }

    for (i = 0; i < n; i++)
    {
        count[nums[i] - '0']++;
    }

    for (i = 0; i <= 9; i++)
    {
        printf("%d\n", count[i]);
    }

    return 0;
}
