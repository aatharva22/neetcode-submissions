class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        sol = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums) - 1

            while right > left:

                sum = nums[right] + nums[left] 

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    sol.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                    
        return sol
