from collections import deque
path = {(0, 0):[]}

def WaterJugbfs(m, n, d):
    queue = deque([(0, 0)])
    visited = set()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        if current[0] == d or current[1] == d:
            return path[current] + [current]
        visited.add(current)
        # Filling first bucket
        if current[0] < m:
            queue.append((m, current[1]))
            path[(m, current[1])] = path[current] + [current]
        #  Filling second bucket
        if current[1] < n:
            queue.append((current[0], n))
            path[(current[0], n)] = path[current] + [current]
        # First bucket has some water
        if current[0] > 0:
            if current[1] < n:
                amount = min(current[0], n - current[1])
                queue.append((current[0]-amount, current[1]+amount))
                path[(current[0]-amount, current[1]+amount)] = path[current] + [current]
        if current[1] > 0:
            if current[0] < m:
                amount = min(current[1], m - current[0])
                queue.append((current[0]+amount, current[1]-amount))
                path[(current[0]+amount, current[1]-amount)] = path[current] + [current]
        if current[0] > 0:
            queue.append((0, current[1]))
            path[(0, current[1])] = path[current] + [current]
        if current[1] > 0:
            queue.append((current[0], 0))
            path[(current[0], 0)] = path[current] + [current]
    return None
m = 4
n = 5
d = 2
result = WaterJugbfs(m, n, d)
if result:
    print("Solution: ")
    for r in result:
        print(r)
else:
    print("Solution not found")
print("Path is: ",path)
