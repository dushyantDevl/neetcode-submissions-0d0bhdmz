class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt, temp = len(s), len(t), []
        if ns < nt: return ""

        tMap = {}
        for c in t: tMap[c] = tMap.get(c, 0) + 1
        
        res = ""

        # 1. Generate all substrings (Brute Force)
        for i in range(ns):
            for j in range(i, ns):
                ss = s[i:j+1]
                
                # 2. Check if ss is valid
                ssMap = {}
                for c in ss: ssMap[c] = ssMap.get(c, 0) + 1
                
                is_valid = True
                for char in tMap:
                    if ssMap.get(char, 0) < tMap[char]:
                        is_valid = False
                        break
                
                # 3. Update result if valid and shorter
                if is_valid:
                    if not res or len(ss) < len(res):
                        res = ss
        return res