class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for i in range(len(strs)):
            arr = [0] * 26
            for j in range(len(strs[i])):  
                arr[ord(strs[i][j]) - ord('a')] += 1
            
            #hashable
            key = tuple(arr)
            if key in hmap:
                hmap[key].append(strs[i])
            else:
                hmap[key] = [strs[i]]
        
        return list(hmap.values())