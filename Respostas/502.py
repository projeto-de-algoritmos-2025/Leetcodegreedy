import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        n = len(projects)

        max_profit_heap = []
        i = 0

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_profit_heap, -projects[i][1])
                i += 1

            if not max_profit_heap:
                break

            w += -heapq.heappop(max_profit_heap)

        return w
