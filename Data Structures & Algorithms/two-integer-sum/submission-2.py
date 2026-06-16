class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        container = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in container:
                return [container[remaining],i]
            else:
                container[num] = i
        

       
                