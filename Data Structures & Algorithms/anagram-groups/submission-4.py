class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for char in strs:
            list1 = [0] * 26
            for ch in char:
                list1[ord(ch) - ord('a')] += 1
            
            if tuple(list1) in hmap:
                hmap[tuple(list1)].append(char)
            else:
                hmap[tuple(list1)] = [char]
            
        return list(hmap.values())


            