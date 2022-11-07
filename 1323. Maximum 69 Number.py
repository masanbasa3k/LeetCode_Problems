class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        nums = []
        s = ''
        for i in range(len(num)):
            nums.append(num[i])
        c = 0
        for i in nums:
            if i == '6' and c == 0:
                c = 1
                i = '9'
            s += i
        return s