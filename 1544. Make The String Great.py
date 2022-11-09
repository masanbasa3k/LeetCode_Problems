class Solution:
    def makeGood(self, s: str) -> str:
        while len(s) > 1:
            
            find = False
            
            for i in range(len(s) - 1):
                curr, curr_next = s[i], s[i+1]
                
                if abs(ord(curr) - ord(curr_next)) == 32: # string number A=65, a=97, a-A=32
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
            if not find:
                break
        return s