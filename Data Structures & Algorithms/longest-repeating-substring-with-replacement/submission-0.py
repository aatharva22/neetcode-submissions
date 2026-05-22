class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # The idea is right moves through the string, till len(substring) - max(values in hmap) > k
        # once this condition is hit, we need to make more replacements, than our budget(k), which is invalid
        # So, then we shrink, move left to the right side, and remove the left pointer element from hmap
        # once we hit a valid substring, len(substring) - max(values in hmap) <= k, we stop and right 
        #moves, we count the longest everytime right moves

        longest = 0
        left = 0
        hmap = {}
        for right in range(len(s)):
            if s[right] in hmap:
                hmap[s[right]] += 1
            else:
                hmap[s[right]] = 1

            #when substring becomes invalid, enter this while and start shrinking
            while (right - left + 1) - (max(hmap.values())) > k:

                hmap[s[left]] -= 1
                left += 1
            
            longest = max(longest, (right - left + 1) )
        
        return longest