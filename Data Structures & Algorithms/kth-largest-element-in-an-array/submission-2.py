class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in range(len(nums)):
            ## make min heap of k element, here min element will be kth largest
            if i < k:
                heapq.heappush(minHeap, nums[i])
            
            ## Compare the new element wtih min element in heap which will make sure new  
            ## element added (after removing the min) maintains the heap of k largest element
            ## We just want element which is greater than any one of minHeap element, so compare
            ## it with the min element in minHeap
            elif nums[i] > minHeap[0]: # minHeap[0] has stored the min element of min Heap
                # remove the min element from minHeap
                heapq.heappop(minHeap)
                # push the new one to maintain heap of k largest element
                heapq.heappush(minHeap, nums[i]) 
        
        # Now minHeap contains k largest element and the kth largest among them will be min from this minHeap
        return heapq.heappop(minHeap)