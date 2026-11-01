from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Count the frequency of each character in both strings
        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        
        # Check if magazine has enough of each character
        for char, count in note_count.items():
            if mag_count[char] < count:
                return False
                
        return True