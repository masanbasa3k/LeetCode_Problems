class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        x = s.split(' ')
        x = x[-1]
        return len(x)