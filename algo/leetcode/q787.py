from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 第一反应，比普通的 dijkstra 算法多一个 max_depth = k 的限制，只要在新节点添加到堆的时候加个 k 的判断即可

        # 然后没过，分析错误用例发现 k 限制不仅影响节点的添加。可能情况：
        # src - mid 有一个选项是 4 站 4 花费，另一个选项是 3 站 5 花费，但前一个先 visite，后面那个花费跟高的路线就不考虑了。
        # 但前面的路径会多一站中转，最后中转数超出，导致路径不可用，而后者却没有被考虑。
        # from collections import defaultdict
        import heapq
        price_table = [[-1 for _ in range(n)] for _ in range(n)]
        for flight in flights:
            price_table[flight[0]][flight[1]] = flight[2]

        visited = dict()
        # (distance, city, transfer_step)
        search_heap = [(0, src, -1)]

        while search_heap:
            distance, current_city, transfer_step = heapq.heappop(search_heap)
            # print(f'pop edge: {(distance, current_city, transfer_step)}')
            if current_city == dst:
                return distance
            visited[current_city] = transfer_step
            for next_city in range(n):
                # 如前分析述，这个 visit 的判断需要额外考虑 transfer_step
                should_visit = next_city not in visited or visited[next_city] > transfer_step
                if should_visit and price_table[current_city][next_city] != -1 and transfer_step < k:
                    # print(f'push edge: {(distance + price_table[current_city][next_city], next_city, transfer_step + 1)}')

                    heapq.heappush(search_heap, (distance + price_table[current_city][next_city], next_city, transfer_step + 1))

        return -1

s = Solution()
res = s.findCheapestPrice(
    11,
    [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]],
    0,
    2,
    4
)

print(res)