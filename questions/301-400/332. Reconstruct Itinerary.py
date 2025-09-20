

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Build graph with min-heap for lexicographical order
        for frm, to in tickets:
            heapq.heappush(graph[frm], to)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                next_stop = heapq.heappop(graph[airport])
                dfs(next_stop)
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]  # Reverse to get the correct order