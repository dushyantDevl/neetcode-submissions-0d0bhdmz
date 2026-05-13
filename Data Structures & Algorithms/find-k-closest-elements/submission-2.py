class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary searching the possible starting positions of the window.
        '''
        Intuition: If the array has length $n$, there are only $n-k+1$ possible windows of size $k$
        i.e we can slide the window on the list $n-k+1$ times
        We want to find the best starting index $i$.
        '''
        n = len(arr)
        l, r = 0, n-k # `r=n-k` make sure it search n-k+1 times (which covers all possible windows and doesn't )

        '''
        Why `l < r` instead of `l <= r`?
            In a standard binary search (like finding the number 7), you use `l <= r` because 7 might 
            be the very last element left, and you need to check that final mid.

            In this problem, we aren't looking for a "target value"; we are narrowing down a range 
            until only one possible starting index remains.
            - while `l < r` means: "Keep narrowing the window until `l` and `r` meet at the same spot."
            - When `l == r`, the search space has collapsed to exactly one index. That index is your answer.
            - If you used `l <= r`, the loop would run one extra time when `l == r`, calculate mid (which 
                would just be equal to `l`), and then you'd have to write extra logic to prevent an 
                infinite loop or index errors.
        '''
        '''
        Why `r = mid` (and not `mid - 1`)?
            This is the most critical part. In standard binary search, if `arr[mid]` isn't your target, 
            you throw it away (`mid - 1`). But here, mid is a candidate.
            
            Look at the logic again:
            `if x - arr[mid] > arr[mid + k] - x`:
            - If this is TRUE: `arr[mid]` is definitively worse than arr[mid + k]. We can safely 
                throw mid away. So, `l = mid + 1`.
            - If this is FALSE: It means arr[mid] is closer to $x$ (or tied) compared to arr[mid + k]. 
                This makes mid a very good candidate for the start of our window.
        '''
        while l < r:
            mid = (l+r)//2
            if x - arr[mid] > arr[mid + k] - x: # when `mid+k`th element is closer discard left part
                l = mid + 1
            else: # discard right part with `mid`th element as potential element
                r = mid
        
        return arr[l:l+k]



