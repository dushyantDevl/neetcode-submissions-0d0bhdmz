class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt = len(s), len(t)
        if ns < nt: return ""

        tMap = {}
        for c in t: tMap[c] = tMap.get(c, 0) + 1
        
        current_unique, required_unique = 0, len(tMap)
        l, windowMap = 0, {}
        ans = ns+1, None, None # min. length, best starting position, best last position (of substring)
        for r in range(ns):
            char_at_r = s[r]
            windowMap[char_at_r] = windowMap.get(char_at_r, 0) + 1
            
            if char_at_r in tMap and windowMap[char_at_r] == tMap[char_at_r]:
                current_unique += 1
            
            while l <= r and current_unique == required_unique:
                char_at_l = s[l]

                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)

                windowMap[char_at_l] -= 1
                if char_at_l in tMap and windowMap[char_at_l] < tMap[char_at_l]:
                    current_unique -=1

                l += 1

        return "" if ans[0] == ns+1 else s[ans[1]:ans[2]+1]