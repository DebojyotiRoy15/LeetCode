#https://leetcode.com/problems/monotonic-array/
#O(n)

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        else:
            h = {'inc': 0, 'dec':0}
            for i in range(len(A) - 1):
                if A[i + 1] >  A[i]:
                    if h['dec'] == 1:
                        return False
                    else:
                        h['inc'] = 1
                elif A[i] > A[i + 1]:
                    if h['inc'] == 1:
                        return False
                    else:
                        h['dec'] = 1
            return True
