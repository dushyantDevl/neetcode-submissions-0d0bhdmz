class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5: return False
        fivesBill, tensBill = 0, 0
        for bill in bills:
            if bill == 5:
                fivesBill += 1
            elif bill == 10:
                tensBill += 1
                if fivesBill > 0:
                    fivesBill -= 1
                else:
                    return False
            else:
                change = bill - 5
                if change == 15 and fivesBill > 0 and tensBill > 0:
                    fivesBill, tensBill = fivesBill-1, tensBill-1
                elif change == 15 and fivesBill >= 3:
                    fivesBill -= 3
                else:
                     return False
        
        return True