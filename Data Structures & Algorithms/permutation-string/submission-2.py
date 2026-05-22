class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        right = len(s1) - 1
        left = 0

        while right < len(s2):
            
            if sorted(s2[left:right+1]) == sorted(s1):
                return True
            right += 1
            left += 1
        
        return False


