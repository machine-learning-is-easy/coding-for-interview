

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Step 1: Create events
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))  # building starts
            events.append((R, 0, 0))   # building ends

        # Step 2: Sort events
        events.sort()

        # Step 3: Use max-heap
        result = []
        max_heap = [(0, float('inf'))]  # (neg height, end)
        prev_height = 0

        for x, negH, R in events:
            # Step 4: Add/remove from heap
            if negH != 0:
                heapq.heappush(max_heap, (negH, R))  # add building
            else:
                # lazily remove buildings that ended
                while max_heap and max_heap[0][1] <= x:
                    heapq.heappop(max_heap)

            # Clean heap top if outdated
            while max_heap and max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            curr_height = -max_heap[0][0]

            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height

        return result