def WaterJugDfs(m, n, d, visited, current, path):
    if current in visited:
        return False
    if current[0] == d or current[1] == d:
        path.append(current)
        return True
    visited.append(current)
    if current[0] < m:
        if WaterJugDfs(m, n, d, visited, (m, current[1]), path):
            path.append(current)
            return True
    if current[1] < n:
        if WaterJugDfs(m, n, d, visited, (current[0], n), path):
            path.append(current)
            return True
    if current[0] > 0:
        if current[1] < n:
            amount = min(current[0], n - current[1])
            if WaterJugDfs(m, n, d, visited, (current[0]-amount, current[1]+amount), path):
                path.append(current)
                return True
    if current[1] > 0:
        if current[0] < m:
            amount = min(current[1], m - current[0])
            if WaterJugDfs(m, n, d, visited, (current[0]+amount, current[1]-amount), path):
                path.append(current)
                return True
    if current[0] > 0:
        if WaterJugDfs(m, n, d, visited, (0, current[1]), path):
            path.append(current)
            return True
    if current[1] > 0:
        if WaterJugDfs(m, n, d, visited, (current[0], 0), path):
            path.append(current)
            return True
    return False

m = 5
n = 4
d = 2
visited = []
current = (0, 0)
path = []
if WaterJugDfs(m, n, d, visited, current, path):
    print("Solution: ")
    for i in range(len(path)-1, -1, -1):
        print(path[i])
else:
    print("Solution not found")
