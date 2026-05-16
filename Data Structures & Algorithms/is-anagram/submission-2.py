class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {} 
        for ch in s:
            if  ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 0
        
        for ch in t:
            if ch not in hmap:
                return False
            else:
                if hmap[ch] == 0:
                    del hmap[ch]
                else:
                    hmap[ch] -= 1
         
        if len(hmap) == 0:
            return True
        else:
            return False