class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = set()
        length = 0
        res = 0
        
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[length])
                length += 1
            temp.add(s[i])
            res = max(res, i - length + 1)
                
        return res
