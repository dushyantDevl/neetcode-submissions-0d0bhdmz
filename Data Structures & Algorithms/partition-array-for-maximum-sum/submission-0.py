class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*n

        def memoization(idx): # returns the max partitions sum (of max length, k) starting from index=idx
            # Base Case
            if idx == n:
                return 0
            
            if dp[idx] != -1:
                return dp[idx]

            partitionLen, largestVal, res = 0, -2147483647, -2147483647

            for i in range(idx, min(n, idx+k)): # `idx+k` should stay less than length of array
                partitionLen += 1
                largestVal = max(largestVal, arr[i])
                # find the current partition sum starting from range [idx, i] then solve the rest i.e. for [i+1, i+k]
                ## e.g. for arr = [2,6,1,4]: n=4,k=2, this recursion will first find the partition sum as following
                ## memoization(3): returns 4 (from [4])
                ## memoization(2): [4] when i=3 & [4,4] when i=2 => returns 4+4=8 [MAX]
                ## memoization(1): when i=2, partitionLen=2,largestVal=6 => 12+memoization(3) => return 12+4=16 [MAX]
                ################## when i=1, partitionLen=1,largestVal=6 => 6+memoization(2) => return 6+8=14.
                ## memoization(0): when i=1, partitionLen=2,largestVal=6 => 12+memoization(2) => return 12+8=20. [MAX]
                ################## when i=0, partitionLen=1,largestVal=2 => 2+memoization(1) => return 2+16=18
                partitionSum = partitionLen * largestVal + memoization(i+1)
                res = max(res, partitionSum)

            dp[idx] = res
            return res


        return memoization(0)
