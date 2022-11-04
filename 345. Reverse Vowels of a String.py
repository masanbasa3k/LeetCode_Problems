class Solution:
    def reverseVowels(self, s: str) -> str:
        b = []
        c =''
        sesli = 'aeiouAEIOU'
        for i in range(len(s)):
            if s[i] in sesli:
                b.append(s[i])
                    
        b = b[::-1]
        for i in range(len(s)):
            if s[i] in sesli:
                c += b[0]
                b.pop(0)
            else:
                c+= s[i]
        return c