class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subsets, subsetSum = [0] * k, total // k
        
        nums.sort(reverse=True)

        def backtrack(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if subsets[i] + nums[idx] <= subsetSum:
                    subsets[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    subsets[i] -= nums[idx]
                
                if subsets[i] == 0:
                    break

            return False

        return backtrack(0)