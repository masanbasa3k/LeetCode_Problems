class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            
            if num in m:
                return [m[num], i]
            else:
                m[complement] = i
