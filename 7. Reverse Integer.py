#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31) - 1 or x < -(2**31):
            return 0
        else:
            rev = 0
            n = x
            if x >= 0:
                buffer = str(n)
                temp = buffer[::-1]
                rev = int(temp)
            elif x < 0:
                n = n*(-1)
                buffer = str(n)
                temp = buffer[::-1]
                temp1 = '-' + temp
                rev = int(temp1)
            if rev > (2**31) - 1 or rev < -(2**31):
                return 0
            else:
                 return rev
