class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}
        left = 0
        right = 0
        longest = 0
        while right < len(s):

            if s[right] in hmap:
                while left < right:
                    if s[left] == s[right]:
                        del(hmap[s[left]])
                        left += 1
                        break
                    del(hmap[s[left]])
                    left += 1
            else:
                hmap[s[right]] = 0
                right += 1
            
            longest = max(longest, right - left)
        
        return longest
