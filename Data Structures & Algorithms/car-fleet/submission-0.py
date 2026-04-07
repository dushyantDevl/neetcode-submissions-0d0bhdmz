class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        stk = []

        for p, s in sorted(pos_speed)[::-1]: # Reverse sorted
            stk.append((target-p) / s) # just stores the remaining time
            if len(stk) >= 2 and stk[-1] <= stk[-2]: # if the 'behind' car is taking lesser time
                stk.pop()
        
        return len(stk)