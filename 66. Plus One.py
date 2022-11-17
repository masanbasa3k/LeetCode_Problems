class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = 0
        digits.reverse()
        for i in range(len(digits)):
            if i != 0:
                t += digits[i] * (10**i)
            else:
                t += digits[i]
        t += 1
        t = str(t)
        s = []
        for i in t:
            s.append(int(i))
        return s
