class Solution(object):
    def findTheDifference(self, s, t):
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))