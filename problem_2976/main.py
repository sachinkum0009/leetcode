"""
2976. Minimum Cost to Convert String I

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
"""

from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # Floyd-Warshall algorithm to find shortest paths between all character pairs
        INF = float('inf')
        # Distance matrix for 26 lowercase letters
        dist = [[INF] * 26 for _ in range(26)]
        
        # Distance from a character to itself is 0
        for i in range(26):
            dist[i][i] = 0
        
        # Build the graph with given transformations
        # If there are multiple edges between same characters, keep the minimum
        for i in range(len(original)):
            src = ord(original[i]) - ord('a')
            dst = ord(changed[i]) - ord('a')
            dist[src][dst] = min(dist[src][dst], cost[i])
        
        # Floyd-Warshall: find shortest paths between all pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate minimum cost to convert source to target
        total_cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                src_idx = ord(source[i]) - ord('a')
                tgt_idx = ord(target[i]) - ord('a')
                if dist[src_idx][tgt_idx] == INF:
                    return -1  # Impossible to convert
                total_cost += dist[src_idx][tgt_idx]
        
        return total_cost


def main():
    source = "abcd"
    target = "acbe"
    original = ["a", "b", "c", "c", "e", "d"]
    changed = ["b", "c", "b", "e", "b", "e"]
    cost = [2, 5, 5, 1, 2, 20]
    res = Solution().minimumCost(source, target, original, changed, cost)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
