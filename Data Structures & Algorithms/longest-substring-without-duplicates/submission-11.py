class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        maxL = 0

        left = 0
        right = 0

        while right < len(s):

            if s[right] not in seen:
                seen.add(s[right])
            

            elif s[right] in seen:

                while s[right] in seen:

                    seen.remove(s[left])
                    left += 1
            
            maxL = max(maxL, right - left + 1)
            seen.add(s[right])
            right += 1
        
        return maxL
        
            
