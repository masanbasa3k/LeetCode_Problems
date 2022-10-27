class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """        
        n = len(img1)
        def checkOut(xShift, yShift):
            num = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= xShift + j < n and 0 <= yShift + i < n:
                        if img1[i + yShift][j + xShift] == 1 and img2[i][j] == 1:
                            num += 1
            return num
        l = list()
        for x in range(-n, n):
            for y in range(-n, n):
                l.append(checkOut(x, y))
        return max(l)