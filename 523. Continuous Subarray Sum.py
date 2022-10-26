import numpy as np

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder = {0 : -1}
        t = 0
        
        for i, n in enumerate(nums):
            t += n
            r = t % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False
                