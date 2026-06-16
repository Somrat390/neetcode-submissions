class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored_nums = set()

        for i in nums:
            if i in stored_nums:
                return True
            stored_nums.add(i)
        return False


        