graph = {'A': ['B', 'C', 'E'],
         'B': ['E', 'F'],
         'C': ['D'],
         'D': ['F'],
         'E': ['C'],
         'F': ['D']}

def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

start_node = input("Enter the starting node: ")
end_node = input("Enter the end node: ")

all_paths = dfs_paths(graph, start_node, end_node)

print("All possible paths between", start_node, "and", end_node, "are:")
for path in all_paths:
    print(path)
