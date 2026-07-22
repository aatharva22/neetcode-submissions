class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxL = 0
        seen = {}
        left = 0
        right = 0

        while right < len(s):

            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1

            if (right-left + 1) - max(seen.values()) > k:

                
            
                while (right-left + 1) - max(seen.values()) > k:

                    if seen[s[left]] == 1:
                        del seen[s[left]]
                    else:
                        seen[s[left]] -= 1
                    
                    left += 1
            
            maxL = max(maxL, right - left + 1)
            right += 1
        
        return maxL
            

                



