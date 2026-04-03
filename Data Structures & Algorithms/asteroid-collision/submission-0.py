class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            if not stk:
                stk.append(asteroid)
            else:
                if asteroid * stk[-1] < 0: # collision condition
                    if abs(asteroid) == abs(stk[-1]):
                        stk.pop()
                    elif abs(asteroid) > abs(stk[-1]):
                        stk.append(asteroid)
                else:
                    stk.append(asteroid)
        return stk