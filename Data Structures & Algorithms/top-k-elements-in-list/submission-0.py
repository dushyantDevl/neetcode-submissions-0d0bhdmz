class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map, res = {}, []
        for num in nums: freq_map[num] = freq_map.get(num, 0) + 1
        sorted_freq_map = dict(sorted(freq_map.items(), key=lambda item:item[1], reverse=True))
        for key in sorted_freq_map.keys():
            if k==0:
                break
            res.append(key)
            k -= 1
        return res

        