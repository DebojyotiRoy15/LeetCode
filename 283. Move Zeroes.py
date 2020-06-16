#https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = []
        c = 0
        for i in range(len(nums)):
	        if nums[i] == 0:
		        c = c + 1
	        else:
		        q.append(nums[i])
        for i in range(len(q)):
	        nums[i] = q[i]
        ind = len(nums) - 1
        while c!= 0:
	        nums[ind] = 0
	        c = c - 1
	        ind = ind - 1
