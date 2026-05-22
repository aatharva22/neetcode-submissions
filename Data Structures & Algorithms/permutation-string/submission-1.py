class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hmap = {}
        for i in range(len(s1)):
            if s1[i] in hmap:
                hmap[s1[i]] += 1
            else : 
                hmap[s1[i]] = 1
        
        hmap1 = {}
        left = 0

        for i in range(len(s1)):
            if s2[i] in hmap1:
                hmap1[s2[i]] += 1
            else : 
                hmap1[s2[i]] = 1
            right = i

        while right < len(s2):
            
            if hmap == hmap1:
                return True

            hmap1[s2[left]] -= 1
            if hmap1[s2[left]] == 0 :
                del hmap1[s2[left]]
            left += 1
            right += 1 

            if right < len(s2) and s2[right] in hmap1:
                hmap1[s2[right]] += 1
            elif right < len(s2) and s2[right] not in hmap1 : 
                hmap1[s2[right]] = 1
  
        return False
            
