class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = defaultdict(list)
        
        for i in strs:
            key = "".join(sorted(list(i)))
            temp[key].append(i)
        
        output = []
        for i in temp.values():
            output.append(i)
            
        return output
                