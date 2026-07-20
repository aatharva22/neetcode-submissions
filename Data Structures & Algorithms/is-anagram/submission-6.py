class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s1 = [0] * 26
        t1 = [0] * 26

        for i in range (len(s)):

            idx1 = ord(s[i]) - ord('a')
            idx2 = ord(t[i]) - ord('a')

            s1[idx1] += 1
            t1[idx2] += 1
        
        for i in range(26):

            if s1[i] != t1[i]:
                return False
        
        return True