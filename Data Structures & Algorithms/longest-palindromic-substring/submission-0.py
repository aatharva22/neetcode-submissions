class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #There can be odd or even length palindrome validate both cases
        #basic idea is expand from center
        start = 0
        end = 0

        def validPalindrome(left,right):
         
            while left >= 0 and right < len(s) and s[left] == s[right]:

                left = left - 1
                right = right + 1
            
            return left + 1 , right - 1
        
        for i in range(len(s)):

            #odd length
            l,r = validPalindrome(i,i)

            if r - l >= end - start:
                end = r 
                start = l 
            
            #even length
            if i+1 < len(s):
                l,r = validPalindrome(i,i+1)

                if r - l >= end - start:
                    end = r 
                    start = l 
        
        return s[start:end+1]



            
