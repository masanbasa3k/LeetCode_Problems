class Solution:
    def reverseWords(self, s: str) -> str: 
        s = s.split(' ')
        s = s[::-1]
        s = list(filter(lambda a: a != '', s))
        x = " ".join(s)
        x = x.strip()
        return x