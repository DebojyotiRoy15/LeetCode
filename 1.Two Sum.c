//https://leetcode.com/problems/two-sum/
//Use of hash table
//O(n) time
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, target, i, result[2], max,key;
    printf("Number of elements in array? \n");
    scanf("%d", &n);
    printf("Target? \n");
    scanf("%d", &target);
    int arr[n];
    for(i=0;i<n;i++)
    {
        printf("arr[%d]: ", i+1);
        scanf("%d", &arr[i]);
    }
    //Hash Table
    key=arr[0];
    for(i=1;i<n;i++)
    {

        if(arr[i]>key)
            key=arr[i];
    }
    max=key;
    max++;
    int hash[max];
    for(i=0;i<max;i++)
    {
        hash[i]=0;
    }
    for(i=0;i<n;i++)
    {
       hash[arr[i]]=1;
    }
    //Check
    for(i=0;i<max;i++)
    {
        if(hash[i]!=0)
        {
            if(hash[target-i]==1)
            {
                result[0]=i;
                result[1]=target-i;
                break;
            }
        }
    }
    printf ("%d %d", result[0], result[1]);
    return 0;
}
