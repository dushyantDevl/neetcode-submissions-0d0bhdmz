class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-f for f in freq.values()]
        heapq.heapify(maxHeap)

        currTime = 0
        q = deque() # pairs of (-f, idleTime)

        while maxHeap or q:
            currTime += 1

            if maxHeap:
                ## decrease the frequency count since maxHeap contains -ve values add 1 
                ## to decrease the frequency
                f = 1 + heapq.heappop(maxHeap)
                if f: # task is still not done since frequency of number of task isn't 0 yet
                    ## to keep track of when certain task can be schedule we should know the
                    ## waiting time w.r.t current ongoing time 
                    q.append((f, currTime + n))

            if q and q[0][1] == currTime:
                heapq.heappush(maxHeap, q.popleft()[0])

        return currTime