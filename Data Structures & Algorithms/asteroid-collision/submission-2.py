class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            # Collisions conditions
            while stk and asteroid < 0 and stk[-1] > 0:
                res = asteroid + stk[-1]
                if res < 0:
                    stk.pop()
                elif res > 0:
                    asteroid = 0 # don't push asteroid in stack
                else:
                    asteroid = 0 # don't push asteroid in stack
                    stk.pop()
            if asteroid:
                stk.append(asteroid)
        return stk