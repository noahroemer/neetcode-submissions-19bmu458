class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        lists = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for key, v in counts.items():
            lists[v].append(key)

        print(lists)

        for i in range(len(lists) - 1, 0, -1):
            for num in lists[i]:
                result.append(num)
                if len(result) == k:
                    return result

            