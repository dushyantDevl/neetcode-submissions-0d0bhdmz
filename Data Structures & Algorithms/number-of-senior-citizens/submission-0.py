class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for dets in details:
            if int(dets[11]+dets[12]) > 60:
                res += 1
        return res