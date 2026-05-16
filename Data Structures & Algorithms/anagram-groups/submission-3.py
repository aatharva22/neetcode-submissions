class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for word in strs:
            label = "".join(sorted(word))
            if label in hmap:
                hmap[label].append(word)
            else:
                hmap[label] = [word]
        
        return list(hmap.values())