class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map= {}
        freq_list = [[] for _ in range(len(nums)+1)] # list of empty lists to store values from nums 
        for num in nums: count_map[num] = count_map.get(num, 0) + 1
        for n,c in count_map.items(): freq_list[c].append(n) # now indexes in freq_list denotes the count of particular element from nums
        res = []
        for i in range(len(freq_list)-1,0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res)==k:
                    return res        