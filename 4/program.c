#include <stdio.h>
//Calculate array size
#define ARRAY_SIZE(a)  sizeof(a)/sizeof(a[0])
// Computes sum all sub-array
long int subArraySum(int arr[], int n)
{
    long int result = 0;
    int i =0,j=0, k= 0;
    // Pick starting point
    for (i=0; i <n; i++)
    {
        // Pick ending point
        for (j=i; j<n; j++)
        {
            for (k = i ; k <= j ; k++)
            {
                result += arr[k];
            }
        }
    }

	for (i=0; i <n; i++)
    {
        // Pick ending point
        for (j=i; j<n; j++)
        {
        }
    }
    return result ;
}
int main()
{
    int arr[] = { 1,3,5};
    //Get array size
    int n = ARRAY_SIZE(arr);
    //Get sum of all sub array
    long int sum  = subArraySum(arr, n) ;
    printf("Sub Array Sum = %d\n",sum);
    return 0;
}