class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        netDegree = defaultdict(int)
        for a1,b1 in trust:
            netDegree[a1] -= 1
            netDegree[b1] += 1

        ## Now if there's a town judge it should have netDegree (or in-degree) value as `n-1`, which implies that 
        ## everybody trusts town judge, it already satisy "town judge trusts nobody" condition otherwise 
        ## `netDegree[a1] -= 1` couldve made the netDegree not equal to `n-1`

        for i in range(1,n+1):
            if netDegree[i] == n-1:
                return i

        return -1