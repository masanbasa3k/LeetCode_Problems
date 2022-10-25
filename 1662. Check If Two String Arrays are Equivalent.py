class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        def open(w):
            s = ''
            for i in range(len(w)):
                s += w[i]
            return s
        
        w1 = open(word1)
        w2 = open(word2)
        
        if w1 == w2:
            return True
        else:
            return False