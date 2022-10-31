import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        n = np.array(nums1+nums2)
        return np.median(n)