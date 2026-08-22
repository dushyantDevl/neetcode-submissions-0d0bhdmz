class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        for freq, char in [(-a,'a'), (-b,'b'), (-c, 'c')]:
            if freq != 0:
                heapq.heappush(maxHeap, (freq, char))

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)

            # Don't append the char to res if its last 2 characters are same as char
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap: # when there are no elements in maxHeap
                    break
                
                freq2, char2 = heapq.heappop(maxHeap)
                res += char2
                freq2 += 1 # decrease the frequency of char (+ bcoz they're stored as -ve)

                if freq2: # character's frequency shouldn't be 0
                    heapq.heappush(maxHeap, (freq2, char2))
            else:
                res += char
                freq += 1

            if freq: # character's frequency shouldn't be 0
                heapq.heappush(maxHeap, (freq, char))

        return res