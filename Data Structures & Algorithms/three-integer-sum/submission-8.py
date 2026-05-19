class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        sol = []

        for i in range(len(nums)):
            # put 0 and duplicate condition
            if nums[i] == nums[i-1] and i>0:
                continue

            target = 0 - nums[i]

            left = i +1
            right = len(nums) - 1

            while left < right:

                

                if nums[left] + nums[right] == target:
                    sol.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while nums[left - 1] == nums[left] and left > i + 1 and left<right:
                        left += 1
                    if right < len(nums) - 1 and right > left:
                        while nums[right + 1] == nums[right]:
                            right -= 1
                elif nums[left] + nums[right] < target:
                    left +=1
                else :
                    right -= 1
        
        return sol
