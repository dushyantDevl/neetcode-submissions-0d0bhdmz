class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        # preserve the original order by storing the index first (with the inner element itself)
        for i in range(n):
            tasks[i].append(i)

        # by default it'll be sorted by first element in inside list i.e. enqueueTimei
        tasks.sort()

        res, minHeap = [], []
        taskIdx, currTime = 0, tasks[0][0]

        while minHeap or taskIdx < n:
            # task can only be schedule if the currTime is >= enqueueTimei of task
            while taskIdx < n and currTime >= tasks[taskIdx][0]:
                processingTimei, ogIdx = tasks[taskIdx][1], tasks[taskIdx][2]
                heapq.heappush(minHeap, (processingTimei, ogIdx))
                taskIdx += 1

            # condition when CPU is idle but there are still some task left in tasks list
            if not minHeap:
                # skip to the next task time (rather than waiting 1 unit at a time)
                currTime = tasks[taskIdx][0]

            # Process the next task with shortest processing time and update currTime
            else:
                processingTimei, ogIdx = heapq.heappop(minHeap)
                currTime += processingTimei
                res.append(ogIdx)

        return res

