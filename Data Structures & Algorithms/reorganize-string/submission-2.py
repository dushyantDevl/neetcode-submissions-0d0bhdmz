class Solution:
    def reorganizeString(self, s: str) -> str:
        charFreq = Counter(s)
        maxHeap = [(-cnt, ch) for ch, cnt in charFreq.items()]
        heapq.heapify(maxHeap)

        ## if some character appears more than half of the string length then there 
        ## aren't enough "other" characters to wedge between them therefore no possible
        ## rearrangement of s exist
        if -maxHeap[0][0] > (len(s) + 1) // 2:
            return ""

        res = []
        while len(maxHeap) >= 2:
            ## pop 2 most frequent character and add to res, they can't be same characters 
            ## bcoz we're remvoing whole [freq, char] list (not just decrementing the freq)
            cnt1, ch1 = heapq.heappop(maxHeap)
            cnt2, ch2 = heapq.heappop(maxHeap)

            res.append(ch1)
            res.append(ch2)

            # Now push the character with their frequency again if its not zero
            if cnt1 + 1 != 0:
                heapq.heappush(maxHeap, (cnt1 + 1, ch1))
            if cnt2 + 1 != 0:
                heapq.heappush(maxHeap, (cnt2 + 1, ch2))

        if maxHeap:
            cnt, ch = maxHeap[0]
            ## When only one char type remains, it's placeable only if it has a single 
            ## occurrence left; otherwise it'd repeat, so return "".
            if -cnt > 1:
                return ""
            res.append(ch)

        return "".join(res)