class Solution:
    #This particular submission is AI generated just to check how much difference a hmap, and a fixed size array would make

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        
        matches = sum(1 for i in range(26) if s1_count[i] == window_count[i])
        
        if matches == 26:
            return True
        
        for right in range(len(s1), len(s2)):
            # Index of the character entering the window
            i_in = ord(s2[right]) - ord('a')
            # Index of the character leaving the window
            i_out = ord(s2[right - len(s1)]) - ord('a')
            
            # Add the new character — check if its match status changes
            window_count[i_in] += 1
            if window_count[i_in] == s1_count[i_in]:
                matches += 1
            elif window_count[i_in] == s1_count[i_in] + 1:
                matches -= 1
            
            # Remove the old character — check if its match status changes
            window_count[i_out] -= 1
            if window_count[i_out] == s1_count[i_out]:
                matches += 1
            elif window_count[i_out] == s1_count[i_out] - 1:
                matches -= 1
            
            if matches == 26:
                return True
        
        return False