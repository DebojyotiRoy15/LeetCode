#https://leetcode.com/problems/sort-colors/

        if len(nums) == 1:
            return nums
        
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums
        
        else:
            hash = {0: 0, 1: 0, 2: 0}
            for num in nums: 
                hash[num] = hash[num] + 1
            k = 0   
            for i in range(0, 3):
                while (hash[i] != 0):
                    nums[k] = i
                    hash[i] = hash[i] - 1
                    k = k + 1
                    
            return nums
