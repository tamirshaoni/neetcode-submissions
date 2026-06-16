class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while(start <= end):
            mid = int((start + end)/2)
            print(mid)
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            if mid_val < target:
                start = mid + 1
            if mid_val > target:
                end = mid - 1
        
        return -1