class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        list1 = [0] * 26
        list2 = [0] * 26

        for ch in s:
            list1[ord(ch) - ord('a')] += 1
        
        for ch in t:
            list2[ord(ch) - ord('a')] += 1
        
        if list1 == list2:
            return True
        else:
            return False
        
