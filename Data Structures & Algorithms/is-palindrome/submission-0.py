class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = "".join((ch.lower() for ch in s if ch.isalnum()))
        

        left,right = 0, len(s1)-1
        while (right > left):
            if s1[right] != s1[left]:
                return False
            left += 1
            right -= 1
        return True
