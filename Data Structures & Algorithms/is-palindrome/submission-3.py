class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        onlyAlnums = "".join(ch.lower() for ch in s if ch.isalnum())
        if len(onlyAlnums) == 0:
            return True

        left = 0
        right = len(onlyAlnums)-1

        while left < right:
            if onlyAlnums[left] != onlyAlnums[right]:
                return False
            left +=1
            right -= 1
        return True