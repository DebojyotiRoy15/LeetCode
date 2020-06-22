#https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c = 0
            else:
                c = c + 1
                res = max(res, c)
        return res
