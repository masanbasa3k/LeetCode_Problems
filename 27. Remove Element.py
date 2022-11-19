class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, c = 0, len(nums)
        
        while i < c:
            if nums[i] == val:
                nums[i] = nums[c - 1]
                c -= 1
            else:
                i += 1
            
        return c