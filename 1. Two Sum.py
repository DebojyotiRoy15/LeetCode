#https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            req_num = target - nums[i]
            if req_num not in dic:
                dic[nums[i]] = i
            else:
                return [dic[req_num], i]
