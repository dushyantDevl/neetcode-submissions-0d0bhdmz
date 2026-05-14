class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt, temp = len(s), len(t), [] 
        for i in range(ns):
            for j in range(i, ns):
                if len(s[i:j+1]) >= nt:
                    temp.append(s[i:j+1])
        tMap, res = [0]*26, ""
        for c in t: tMap[ord(c.lower())-ord('a')] += 1
        for ss in temp:
            count = 0
            ssMap = [0]*26
            for c in ss: ssMap[ord(c.lower())-ord('a')] += 1
            for i in range(26):
                if ssMap[i] != 0 and ssMap[i] == tMap[i]: count += 1
            if count >= nt:
                if not res:
                    res = ss
                else:
                    res = ss if len(ss) < len(res) else res
        return res