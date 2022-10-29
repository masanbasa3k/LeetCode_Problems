import numpy as np
class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        times = list(zip(plantTime, growTime))
        
        times.sort(key = lambda x: -x[1])
        day = 0
        
        cur = 0
        
        for plant, grow in times:
            cur += plant
            day = max(day, cur + grow)
            
        return day