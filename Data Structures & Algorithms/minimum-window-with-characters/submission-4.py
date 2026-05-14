class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt = len(s), len(t)
        if ns < nt: return ""

        tMap = {}
        for c in t: tMap[c] = tMap.get(c, 0) + 1
        required_unique = len(tMap)
        
        res = ""

        for i in range(ns):
            ssMap = {}
            formed_unique = 0
            
            for j in range(i, ns):
                char = s[j]
                ssMap[char] = ssMap.get(char, 0) + 1
                
                # If this character just reached the required frequency in t
                if char in tMap and ssMap[char] == tMap[char]:
                    formed_unique += 1
                
                # Check if all unique characters in t are present in current window
                if formed_unique == required_unique:
                    ss = s[i : j+1]
                    if not res or len(ss) < len(res):
                        res = ss
                    break # Optimization: Since we found the shortest window for this 'i', stop 'j'
        return res