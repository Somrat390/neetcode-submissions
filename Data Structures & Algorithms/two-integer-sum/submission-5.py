class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_mate = {}

        for i,num in enumerate(nums):
            mate = target - num

            if mate in my_mate:
                return [my_mate[mate], i]
            my_mate[num] = i

            
        
            
        