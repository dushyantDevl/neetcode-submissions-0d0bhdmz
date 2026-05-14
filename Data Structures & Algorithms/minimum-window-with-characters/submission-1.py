class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt, temp = len(s), len(t), [] 
        for i in range(ns):
            for j in range(i, ns):
                if len(s[i:j+1]) >= nt:
                    temp.append(s[i:j+1])
        tMap, res = {}, ""
        for c in t: tMap[c] = tMap.get(c, 0) + 1
        for ss in temp:
            count, ssMap = 0, {}
            for c in ss: ssMap[c] = ssMap.get(c, 0) + 1
            for k in ssMap:
                if k in tMap and ssMap[k] == tMap[k]: count += 1
            if count >= nt:
                if not res:
                    res = ss
                else:
                    res = ss if len(ss) < len(res) else res
        return res