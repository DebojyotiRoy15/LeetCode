#https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other = target - nums[i]
            numsAux = nums[i+1:]
            if other in numsAux:
                ind = numsAux.index(other)
                return [i, ind+i+1]
