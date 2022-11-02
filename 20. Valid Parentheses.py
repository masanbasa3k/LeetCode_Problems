class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(',']':'[','}':'{'}
        
        for i in s:
            if i in d:
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False