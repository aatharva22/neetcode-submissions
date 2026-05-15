class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for str in strs:
            label = "".join(sorted(str)) # the label is sorted order of the string        
            if label in hmap:
                hmap[label].append(str)
            else:
                hmap[label] = [str]
        
        return list(hmap.values())