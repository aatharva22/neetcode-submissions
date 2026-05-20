class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}
        left = 0
        right = 0
        longest = 0

        while right < len(s):

            if s[right] in hmap :
                # using max so left doesn't jump back unnecessarily
                left = max(hmap[s[right]] + 1 , left) 
                hmap[s[right]] = right
            else : 
                hmap[s[right]] = right
                
            longest = max (longest, (right - left + 1))
            right += 1
            
        
        return longest