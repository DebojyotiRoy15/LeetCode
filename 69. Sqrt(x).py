#https://leetcode.com/problems/sqrtx/
#O(logn)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        else:
            left = 0
            right = x
            while(left<=right):
                mid = (left + right)//2
                if mid*mid == x:
                    return mid
                if mid*mid > x:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
