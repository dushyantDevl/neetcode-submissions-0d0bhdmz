class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # “Combination Sum IV” is misnamed, it counts ordered sequences 
        # (permutations), not combinations, that's why for `nums = [1,2,3]`, 
        # `target = 4` the answer is `7`: (1,1,2), (1,2,1), (2,1,1), (2,2), 
        # (1,3), (3,1), (1,1,1,1).otherwise the answer could've been 4 by 
        # counting "(1,1,2), (1,2,1), (2,1,1)" and "(1,3), (3,1)" 1 time

        # therfore, the take/notTake-over-sorted-indices pattern inherently 
        # counts unordered multisets. By walking idx from high to low and only 
        # ever reusing the current index, you’ve imposed a fixed element 
        # ordering, which collapses (1,3) and (3,1) into one. So this structure 
        # tops out at counting combinations (4 here), never the 7 the problem 
        # wants. There’s no fix to this template — the counting has to be driven 
        # by the running sum, not by element indices.
        
        nums.sort()
        dp = [-1] * (target+1)
        dp[0] = 1 # Base Case
        
        def memoization(total):
            # Caching
            if dp[total] != -1:
                return dp[total]

            res = 0
            for num in nums:
                ## Since the list is sorted, we can break the loop early to 
                ## avoid numbers greater than the remaining total
                if total < num:
                    break
                res += memoization(total - num)
            dp[total] = res
            return res

        return memoization(target)

'''
Dry Run of the test case:
dfs(4)
├─ num=1 → dfs(3)
│         ├─ num=1 → dfs(2)
│         │         ├─ num=1 → dfs(1)
│         │         │         ├─ num=1 → dfs(0) = 1        memo[1]=1
│         │         │         └─ num=2 → 1<2, break
│         │         ├─ num=2 → dfs(0) = 1
│         │         ├─ num=3 → 2<3, break
│         │         └─ memo[2] = 1+1 = 2
│         ├─ num=2 → dfs(1) = 1   (memo hit)
│         ├─ num=3 → dfs(0) = 1
│         └─ memo[3] = 2+1+1 = 4
├─ num=2 → dfs(2) = 2   (memo hit)
├─ num=3 → dfs(1) = 1   (memo hit)
└─ memo[4] = 4+2+1 = 7
'''