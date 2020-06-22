#https://leetcode.com/problems/majority-element/
#O(nlogn)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        pos = math.floor((len(nums))/2)
        element = nums[pos]
        return element
