class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        s = (n * (n + 1)) // 2
        st = sum(set(nums))
        k = sum(nums)
        return [k-st, s-st]