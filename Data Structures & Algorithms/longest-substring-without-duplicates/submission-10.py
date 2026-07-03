class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}

        left = 0
        right = 0
        longest = 0

        while right < len(s):

            if s[right] in hmap:

                while s[right] in hmap:
                    del(hmap[s[left]])
                    left += 1
                hmap[s[right]] = 1
                longest = max(longest, right - left + 1)
                right += 1


            else:
                hmap[s[right]] = 1
                longest = max(longest, right - left + 1)
                right += 1
        
        return longest
            