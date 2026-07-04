class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subsets, subsetSum = [0] * k, total // k
        if nums[0] > subsetSum:
            return False
        
        nums.sort(reverse=True)

        def backtrack(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if i > 0 and subsets[i] == subsets[i-1]: # skip duplicates
                    continue
                if subsets[i] + nums[idx] <= subsetSum:
                    subsets[i] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    subsets[i] -= nums[idx]
                
                if subsets[i] == 0:
                    break

            return False

        return backtrack(0)