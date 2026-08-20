class Solution:
    def reorganizeString(self, s: str) -> str:
        charFreq = Counter(s)
        maxHeap = [[-freq, char] for char,freq in charFreq.items()]
        heapq.heapify(maxHeap)
        
        res = ""
        prev = None
        # [frequency of char in previous round, char from previous round that was added in res]
        
        while maxHeap or prev:
            ## Below condition means the only character left to place is the one we just 
            ## placed — so the next char would have to be identical to the last. 
            ## No valid arrangement exists.
            if prev and not maxHeap:
                return ""

            freq, char = heapq.heappop(maxHeap)
            res += char
            freq += 1 # decrease frequency of char (-ve bcoz of -ve frequency stored in maxHeap)

            ## Before deciding where the current char goes, look at prev — the char from 
            ## the previous round. If it exists and still has count left, push it back into 
            ## the heap now. It has served its one-round timeout, so it's eligible again.
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None # char can be refilled with the current char in the next line.

            ## We pop the current char first (that pop can't return prev, because prev isn't 
            ## in the heap). Then we return prev to the heap. So on the next iteration, both 
            ## the current char and the released prev are candidates — but the current char 
            ## is now the one held out. They alternate through the box, which guarantees no 
            ## two identical chars land adjacently.

            ## put the current char into prev (if it still has count left), so it sits out 
            ## the next round and we can avoid putting that in res again
            if freq != 0:
                prev = [freq, char]

        return res