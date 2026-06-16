class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]