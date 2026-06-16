class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        freq_bucket = [[] for _ in range(len(nums)+1)]
        for key, val in freq.items():
            freq_bucket[val].append(key)
        res = []
        for i in range(len(freq_bucket)-1,0,-1):
            for n in freq_bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

        