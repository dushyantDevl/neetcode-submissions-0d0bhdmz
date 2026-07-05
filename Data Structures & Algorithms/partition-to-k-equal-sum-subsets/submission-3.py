class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ## Every num has k choices here and the way recursion tree will divide will depend on k
        ## i=0 -> k chioces then each of these choice will again have choices i.e. k, k^2, k3
        ## so its a GP with common ratio k, so T.C will be sum of this GP
        ## $$a\frac{(r^{n}-1)}{(r-1)}$$ i.e approx k^n -> worst case scenario

        ## Here in the following method we'll ask each element if it can be included in some
        ## particular bucket (out of all k) or not then go to next element and do the same
        ## if 1 bucket is filled check for other but start with starting index since its possible
        ## we didn't pick a element last time, so we also have to keep track of the elements we've
        ## picked until now

        ## This method might give TLE but it's right!

        subsetsTotalSum = sum(nums)
        if subsetsTotalSum % k != 0:
            return False
        
        reqSum = subsetsTotalSum // k

        alreadyIncluded = [False] * len(nums)

        def helper(idx, bucketNum, currenSubsetSum):
            # Base Cases
            if bucketNum > k:
                return True # All buckets are filled
            
            if currenSubsetSum == reqSum:
                ## move to next bucket but start from 1st index again, and 
                ## currenSubsetSum will also start from 0 now
                return helper(0, bucketNum+1, 0)
            
            if currenSubsetSum > reqSum:
                return False
            
            if idx >= len(nums):
                return False

            if alreadyIncluded[idx]:
                return helper(idx+1, bucketNum, currenSubsetSum) # move the pointer to next element
            else:
                currenSubsetSum += nums[idx]
                alreadyIncluded[idx] = True
                includingCase = helper(idx+1, bucketNum, currenSubsetSum)

                # Skip the element (not pick in a bucket)
                currenSubsetSum -= nums[idx]
                alreadyIncluded[idx] = False
                notIncludingCase = helper(idx+1, bucketNum, currenSubsetSum)

                return includingCase or notIncludingCase

        return helper(0, 1, 0)
