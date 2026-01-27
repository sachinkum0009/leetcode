"""
3650. Minimum Cost Path with Edge Reversals

You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.
"""

from typing import List
import heapq
from collections import defaultdict


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # 0: Normal edges, 1: Reversed edges
        adj = [defaultdict(list), defaultdict(list)]
        for u, v, w in edges:
            adj[0][u].append((v, w))
            adj[1][v].append((u, w))
            
        # pq stores: (cumulative_cost, current_node, is_reversed)
        # is_reversed: 0 for normal, 1 for flipped
        pq = [(0, 0, 0)]
        
        # dist[(node, is_reversed)] = min_cost
        dist = {}

        while pq:
            d, u, state = heapq.heappop(pq)

            if u == n - 1:
                return d

            if dist.get((u, state), float('inf')) <= d:
                continue
            dist[(u, state)] = d

            # 1. Continue moving in the CURRENT state (Normal or Reversed)
            for v, weight in adj[state][u]:
                # In reversed state, cost is 2 * weight (as per your original logic)
                move_cost = weight if state == 0 else 2 * weight
                if d + move_cost < dist.get((v, state), float('inf')):
                    heapq.heappush(pq, (d + move_cost, v, state))

            # 2. Flip the switch to change state (Normal <-> Reversed)
            # This happens at the current node 'u' with 0 traversal cost
            new_state = 1 - state
            if d < dist.get((u, new_state), float('inf')):
                heapq.heappush(pq, (d, u, new_state))

        return -1


def main():
    n = 4
    edges = [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]
    res = Solution().minCost(n, edges)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
