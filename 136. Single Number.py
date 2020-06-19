#https://leetcode.com/problems/single-number/
#O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                h[nums[i]] = h[nums[i]] + 1
        for i, j in h.items():
            if j == 1:
                p = i
                break
        return p
