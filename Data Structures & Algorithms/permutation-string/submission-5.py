class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

            
        ords1 = [0] * 26
        ordAns = [0] * 26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            ords1[index] += 1

            idx2 = ord(s2[i]) - ord('a')
            ordAns[idx2] += 1

        if ords1 == ordAns:
            return True

        for i in range(len(s1) , len(s2)):

            remidx = ord(s2[i-len(s1)]) - ord('a')
            addidx = ord(s2[i]) - ord('a')

            ordAns[remidx] -= 1
            ordAns[addidx] += 1

            if ords1 == ordAns:
                return True
        
        return False



        

