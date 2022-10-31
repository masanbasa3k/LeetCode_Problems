class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        xstr_reverse = xstr[::-1]
        
        if xstr == xstr_reverse:
            return True
        else:
            return False