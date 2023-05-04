from collections import deque

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['E', 'F'],
    'C': ['D'],
    'D': ['F'],
    'E': ['C'],
    'F': ['D']
}

# Function to perform BFS
def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in path:
                if neighbour == end:
                    return path + [neighbour]
                else:
                    queue.append((neighbour, path + [neighbour]))
    return None

start_node = input("Enter the start node: ")
end_node = input("Enter the end node: ")

path = bfs(graph, start_node, end_node)

if path is None:
    print("No path exists between", start_node, "and", end_node)
else:
    print("Shortest path between", start_node, "and", end_node, "is:", ' -> '.join(path))
