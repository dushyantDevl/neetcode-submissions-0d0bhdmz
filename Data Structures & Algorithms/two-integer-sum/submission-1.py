class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map, ans = {}, []
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            if map.get(target-nums[i]) is not None:
                if i<map[target-nums[i]]:
                    ans.append(i)
                    ans.append(map[target-nums[i]])
                    break
                elif i<map[target-nums[i]]:
                    ans.append(map[target-nums[i]])
                    ans.append(i)
                    break
        return ans

