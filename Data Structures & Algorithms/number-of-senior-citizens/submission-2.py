class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for dets in details:
            tenthPlace = ord(dets[11]) - ord('0')
            unitPlace = ord(dets[12]) - ord('0')
            age = tenthPlace * 10 + unitPlace

            if age > 60:
                res += 1
                
        return res