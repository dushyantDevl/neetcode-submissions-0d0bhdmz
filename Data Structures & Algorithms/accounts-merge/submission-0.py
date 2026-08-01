class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        mailToNode = {}
        ds = DisjoinSet(n)
        for node in range(n):
            for i in range(1, len(accounts[node])):
                if accounts[node][i] not in mailToNode:
                    mailToNode[accounts[node][i]] = node
                else:
                    ds.unionBySize(node, mailToNode[accounts[node][i]])

        mergedMail = [[] for _ in range(n)]
        for mail, node in mailToNode.items():
            node = ds.findRootParent(node)
            mergedMail[node].append(mail)
        
        res = []
        for i in range(n):
            if len(mergedMail[i]) == 0: continue
            mergedMail[i].sort()
            temp = []
            temp.append(accounts[i][0])
            for mail in mergedMail[i]:
                temp.append(mail)
            res.append(temp)

        return res


class DisjoinSet:
    def __init__(self, N) -> None:
        self._parent = [i for i in range(N+1)]
        self._size = [1] * (N+1)

    def findRootParent(self, node):
        if self._parent[node] != node:
            self._parent[node] = self.findRootParent(self._parent[node])
        return self._parent[node]

    def unionBySize(self, u, v):
        uParent, vParent = self.findRootParent(u), self.findRootParent(v)

        if uParent == vParent: return
        if self._size[uParent] > self._size[vParent]:
            self._parent[vParent] = uParent
            self._size[uParent] += self._size[vParent]
        else:
            self._parent[uParent] = vParent
            self._size[vParent] += self._size[uParent]