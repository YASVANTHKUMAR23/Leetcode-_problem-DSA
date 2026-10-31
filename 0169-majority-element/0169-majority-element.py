from collections import Counter

      
class Solution(object):
    def majorityElement(self, nums):
        freq = Counter(nums)
        for i in freq:
            if freq[i] > len(nums) / 2:
                return i
        
        