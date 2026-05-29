class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []

        for ch in s:
            if ch.isalnum():
                s1.append(ch.lower())
        s2 = "".join(s1)
        right = len(s2) - 1
        left = 0

        while left < right:

            if s2[left] != s2[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True

