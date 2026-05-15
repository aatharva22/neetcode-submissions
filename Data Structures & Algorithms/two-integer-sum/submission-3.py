class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        ans = []
        for i in range(len(nums)):
            hmap[nums[i]] = i

        for i in range(len(nums)):
            if ((target - nums[i]) in hmap) and hmap[(target - nums[i])] != i :
                ans.append(i)
                ans.append(hmap[target-nums[i]])
                return sorted(ans)
             