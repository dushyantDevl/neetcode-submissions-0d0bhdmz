class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_og = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp not in sorted_to_og:
                sorted_to_og[temp] = [word]
            else:
                sorted_to_og[temp].append(word)
        return list(sorted_to_og.values())