"""
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
"""
def find_valid_path(n, edges, source, destination):
    visited = [False] * n
    visited[source] = True

    flag = True
    while flag:
        flag = False
        for edge in edges:
            if visited[edge[0]] != visited[edge[1]]:
                visited[edge[0]] = True
                visited[edge[1]] = True
                flag = True

            if visited[destination]:
                return True
    return False
