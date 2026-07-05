class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hmap = {}

        left = 0
        right = 0
        longest = 0

        while right < len(s):

            if s[right] in hmap:
                hmap[s[right] ] += 1
            else :
                hmap[s[right] ] = 1
            
            if (right - left + 1 - max(hmap.values()) <= k) :

                longest = max(longest, right - left + 1)
                right += 1
            
            else:

                while (right - left + 1 - max(hmap.values()) > k) and left <= right:

                    if hmap[s[left]] == 1:
                        del hmap[s[left]]
                    else:
                        hmap[s[left]] -= 1
                    left += 1
                right += 1
                
        return longest



