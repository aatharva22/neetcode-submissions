class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2
            #The rotation is in clockwise direction so when mid > left and mid>right
            # the drop will be in mid, right
            if nums[mid] > nums[right]:
                #drop happened here, so ans in mid+1, right region
                left = mid + 1
            else:
                #drop did not happen in mid, right. So it must have happened in 
                # left to mid
                right = mid

        return nums[right]   

