class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        for i in range(len(nums)):
            val = nums[i]
            nums[i] = 1
            product = math.prod(nums)
            product_list.append(product)
            nums[i] = val

        return product_list
