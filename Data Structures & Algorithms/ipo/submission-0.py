class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = [] # stores only the projects we can afford (with max profit at top)
        
        ## minCapital will help us in picking min. capital project first since we can't pick
        ## project which has more capital cost then if we can do the max profit project in
        ## that available capital (i.e. capital value less than equal to w) we can choose
        ## the max profit project from maxProfit max heap
        minCapital = [(cap,pro) for cap,pro in zip(capital,profits)]
        heapq.heapify(minCapital)

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                _, pro = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -pro)

            # when we can't pick the project for which we don't have enough capital
            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit)

        return w