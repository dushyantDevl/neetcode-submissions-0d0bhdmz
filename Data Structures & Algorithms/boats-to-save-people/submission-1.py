class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r, boats = 0, len(people)-1, 0
        while l <= r:
            # if lighter person can fit in with heavier one, put him with heavier
            if people[l] + people[r] <= limit:
                l += 1
            # just take the heaviest person regardless
            boats, r = boats+1, r-1
        return boats