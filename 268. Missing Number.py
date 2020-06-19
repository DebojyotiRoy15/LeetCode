#https://leetcode.com/problems/missing-number/
#O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum =(n*(n+1))//2
        sum_real = 0
        for i in range(len(nums)):
            sum_real = sum_real + nums[i]
        diff = abs(sum_real - sum)
        return diff
