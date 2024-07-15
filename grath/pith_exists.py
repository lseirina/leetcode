"""
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
"""
from collections import defaultdict

def find_valid_path(n, edges, source, destination):
    grath = defaultdict(list)

    for u, v in edges:
        grath[u].append(v)
        grath[v].append(u)

    def dfs(node, visited):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in grath[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True

        return False

    visited = set()
    return dfs(source, visited)


print(find_valid_path(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))



















# def find_valid_path(n, edges, source, destination):
#     visited = [False] * n
#     visited[source] = True

#     flag = True
#     while flag:
#         flag = False
#         for edge in edges:
#             if visited[edge[0]] != visited[edge[1]]:
#                 visited[edge[0]] = True
#                 visited[edge[1]] = True
#                 flag = True

#             if visited[destination]:
#                 return True
#     return False
