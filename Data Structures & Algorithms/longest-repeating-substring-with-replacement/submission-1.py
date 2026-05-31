class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        right = 0
        left = 0
        longest = 0
        hmap = {}
        while right < len(s):
            
            if s[right] in hmap:

                hmap[s[right]] += 1
            else:
                hmap[s[right]] = 1
            
            right += 1

            if right - left  - max(hmap.values()) > k:
                while right - left - max(hmap.values()) > k:
                    if hmap[s[left]] == 1:
                        del(hmap[s[left]])
                    else: 
                        hmap[s[left]] -= 1
                    left += 1
            
            longest = max(longest, right-left)
        
        return longest

            