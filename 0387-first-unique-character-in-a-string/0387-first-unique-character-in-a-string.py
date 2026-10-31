from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)
        for i in s:
            if freq[i] == 1:
                return s.index(i)
        return -1
        
        