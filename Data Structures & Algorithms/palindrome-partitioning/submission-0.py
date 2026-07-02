class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, parts = [], []
        
        def backtrack(i, n):
            if i == n:
                res.append(parts.copy())
                return

            for j in range(i, n):
                # only do the further recursion call when each part(substring) is a palindrome
                if (self.isPalindrome(s, i, j)):
                    parts.append(s[i:j+1]) # append each part of parts (all parts -> partitions)
                    # call for each substring, from index 0->0,0->1,0->2,1->1,1->2,2->2 (for n=3)
                    backtrack(j+1, n)
                    parts.pop()

        backtrack(0, len(s))
        return res

    def isPalindrome(self, s: str, l:int, r:int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1

        return True